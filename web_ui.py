import streamlit as st
from swift.llm import get_model_list_client, XRequestConfig, inference_client

# page config
st.set_page_config(
    page_title="扁仓中医大模型",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# title
st.title('扁仓中医大模型👨🏻‍⚕️')
st.caption('本应用基于扁仓中医大模型，模型生成的中医内容仅作为辅助工具，不能替代实际的医疗诊断和治疗。')

# API
port = "8090"
@st.cache_data
def get_model_type():
    model_list = get_model_list_client(port=port)
    model_type = model_list.data[0].id
    print(f'API model_type: {model_type}')
    return model_type


model_type = get_model_type()

INITIAL_MESSAGE = [
    {
        "role": "assistant",
        "content": "你好，我是扁仓中医大模型！有什么需要帮忙的吗？ 😊",
    }
]

if st.sidebar.button("清除历史"):
    del st.session_state['messages']
    st.session_state["messages"] = INITIAL_MESSAGE
    del st.session_state["history"]
    st.session_state["history"] = []

if "messages" not in st.session_state.keys():
    st.session_state["messages"] = INITIAL_MESSAGE

if "history" not in st.session_state.keys():
    st.session_state["history"] = []



for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

def stream_chat(stream):
    for chunk in stream:
        response = chunk.choices[0].delta.content
        yield response


if prompt := st.chat_input("➡在此输入你的问题。"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        request_config = XRequestConfig(stream=True, seed=42)
        stream_resp = inference_client(model_type, prompt, st.session_state.history, request_config=request_config, port=port)
        response = st.write_stream(stream_chat(stream_resp))

    st.session_state.messages.append({"role": "assistant", "content": response})
    st.session_state.history.append([prompt, response])


