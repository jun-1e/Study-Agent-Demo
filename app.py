
import streamlit as st

from main import init_chat, chat


st.set_page_config(
    page_title="Study Agent",
    page_icon="🤖",
    layout="centered",
)

st.title("🤖 Study Agent")

# 初始化会话状态
if "messages" not in st.session_state:
    st.session_state.messages = init_chat()

# 显示已有聊天记录
for message in st.session_state.messages:
    role = message.get("role")

    if role not in ("user", "assistant"):
        continue

    content = message.get("content")

    if not content:
        continue

    with st.chat_message(role):
        st.markdown(content)

# 接收用户输入
if prompt := st.chat_input("请输入你的问题..."):
    # 显示本次用户输入
    with st.chat_message("user"):
        st.markdown(prompt)

    # 调用 Agent
    with st.chat_message("assistant"):
        with st.spinner("正在思考..."):
            try:
                answer, updated_messages = chat(
                    prompt,
                    st.session_state.messages,
                )

                st.session_state.messages = updated_messages
                st.markdown(answer)

            except Exception as e:
                st.error(f"运行出错：{e}")
