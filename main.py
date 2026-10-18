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

history = events.read_files("history")
events.write_files(history,"history_copy")
messages = history[-3:]
print(messages)
# K_msg = events.read_files("userFiles")
# events.write_files(K_msg,"userFiles_copy")


user_input = input("You:")
messages.append({
    "role": "user",
    "content": user_input
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

    print(message.content)

    # 没有工具调用，说明已经可以直接回答
    if not message.tool_calls:
        if user_input == "exit":
            for his in messages[3:]:
                history.append(his)
            events.write_files(history,"history")
            break
        messages.append({
            "role": "user",
            "content": user_input
        })
        messages.append({
            "role": "assistant",
            "content": message.content,
            "reasoning_content": message.reasoning_content,
        })
        user_input = input("You:")
        continue        

        
    # 保存 AI 本轮的回答
    events.append_msg(messages,message)

    available_functions = {
        "calculator": tools.calculator,
        "savefile": tools.savefile,
        "ref_userfile": tools.ref_userfile
    }

    # 执行 AI 请求的所有工具
    for tool_call in message.tool_calls:

        function_name = tool_call.function.name

        function_to_call = available_functions[function_name]

        function_args = json.loads(
            tool_call.function.arguments
        )

        function_response = function_to_call(
            **function_args
        )

        messages.append({
            "role": "tool",
            "tool_call_id": tool_call.id,
            "content": str(function_response)
        })