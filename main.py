
import os
import json

from openai import OpenAI
from dotenv import load_dotenv

from tools import tools
from Func_Lists import functions
from events import events


load_dotenv()

client = OpenAI(
    api_key=os.environ["DEEPSEEK_API_KEY"],
    base_url="http://localhost:8000/v1",
)

# AI 可以调用的工具
available_functions = {
    "calculator": tools.calculator,
    "savefile": tools.savefile,
    "ref_userfile": tools.ref_userfile,
}


def init_chat():
    """加载历史消息，供 Streamlit 前端初始化会话。"""
    try:
        history = events.read_files("history")

        # 仅在读取成功后更新备份
        events.write_files(history, "history_copy")

    except (json.JSONDecodeError, ValueError) as e:
        print(f"历史记录读取失败：{e}")
        raise
    
    messages = history[-20:]

    return messages


def chat(user_input, messages):
    """
    接收前端输入，运行一轮 Agent 对话。
    返回：(AI 最终回答, 更新后的 messages)
    """
    messages = list(messages)

    # 记录本轮开始的位置，方便只保存新增消息
    start_index = len(messages)

    messages.append({
        "role": "user",
        "content": user_input,
    })

    while True:
        response = client.chat.completions.create(
            model="deepseek-v4-flash",
            messages=messages,
            tools=functions,
            tool_choice="auto",
            extra_body={
                "thinking": {
                    "type": "enabled"
                }
            }
        )

        message = response.choices[0].message

        # 没有工具调用，说明本轮回答完成
        if not message.tool_calls:
            answer = message.content or ""

            messages.append({
                "role": "assistant",
                "content": answer,
                "reasoning_content": message.reasoning_content,
            })

            # 将本轮新增的用户消息、工具调用及回答保存到历史文件
            history = events.read_files("history")
            history.extend(messages[start_index:])
            events.write_files(history, "history")

            return answer, messages

        # 保存 AI 的工具调用消息
        events.append_msg(messages, message)

        # 执行 AI 请求的所有工具
        for tool_call in message.tool_calls:
            function_name = tool_call.function.name

            if function_name not in available_functions:
                function_response = (
                    f"Error: Unknown tool '{function_name}'"
                )
            else:
                function_to_call = available_functions[function_name]

                try:
                    function_args = json.loads(
                        tool_call.function.arguments
                    )

                    function_response = function_to_call(
                        **function_args
                    )
                except Exception as e:
                    function_response = f"Tool execution error: {e}"

            messages.append({
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": str(function_response),
            })
