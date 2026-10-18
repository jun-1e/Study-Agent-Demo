
import streamlit as st

st.set_page_config(
    page_title="Study Agent",
    page_icon="🤖",
    layout="centered"
)

st.title("Study Agent")
st.write("你好！这是我的第一个 AI Agent 网页。")

# 初始化聊天记录
if "messages" not in st.session_state:
    st.session_state.messages = []

# 显示已有的聊天记录
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# 接收用户输入
prompt = st.chat_input("请输入你的问题...")

if prompt:
    # 保存并显示用户消息
    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    with st.chat_message("user"):
        st.write(prompt)

    # 暂时用固定回复模拟 AI
    response = f"我收到了你的消息：{prompt}"

    # 保存并显示 AI 回复
    st.session_state.messages.append({
        "role": "assistant",
        "content": response
    })

    with st.chat_message("assistant"):
        st.write(response)

