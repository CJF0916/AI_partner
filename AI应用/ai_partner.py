import streamlit as st  # 用于构建web应用界面
import os  # 导入os库，用于读取环境变量中的API密钥
from openai import OpenAI  # 用于调用DeepSeek大模型

# 页面布局
st.set_page_config(
    page_title="AI智能伴侣",
    page_icon="🤖",
    # 布局
    layout="wide",
    initial_sidebar_state="expanded",  # 侧边栏
    menu_items={  # 菜单
        'About': "# 我是🤖AI智能伴侣!"
    }
)
# 大标题
st.title("🤖AI智能伴侣🚀")

st.logo("AI应用/resources/logo.png")
# 创建与DeepSeek大模型交互的客户端对象
# 从环境变量中读取DEEPSEEK_API_KEY作为API密钥
# 指定DeepSeek的API基础地址
client = OpenAI(
    api_key=os.environ.get('DEEPSEEK_API_KEY'),
    base_url="https://api.deepseek.com")
# 定义系统提示词，用于给AI设定角色和回答风格
system_prompt = "你是一名非常可爱的AI助理，你的名字叫小甜甜，请你使用温柔可爱的语气回答用户的问题"

# 初始化聊天信息列表（存储对话历史）
if "messages" not in st.session_state:
    st.session_state.messages = [] #消息列表

# 遍历session_state中存储的所有历史消息
for message in st.session_state.messages:
    # 根据消息的角色（user/assistant）显示对应的气泡
    role = message["role"]
    content = message["content"]
    with st.chat_message(role): #创建什么角色的会话框
        st.write(content)  #在会话框填写内容
# 创建聊天输入框，提示用户输入问题
problem = st.chat_input("请输入您要问的问题")
if problem:
    st.chat_message("user").write(problem)
# 在控制台打印用户输入的内容，方便调试
    print("---------> 调用AI大模型，提示词：", problem)

  # !!将用户的消息添加到session_state的历史消息列表中
    st.session_state.messages.append({"role":"user","content":problem})
#deepseek 回答问题:调用deepseek大模型
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": system_prompt},
            #显示用户和ai的所有消息记录,格式如下:
            #{"role": "user", "content": "你是谁"},
            #解包,解列表messages[{里面是字典key:value},{}]
            *st.session_state.messages
        ],
        stream=False,     # 不使用流式输出（一次性返回完整结果）

        )
    # 在控制台打印大模型返回的结果，方便调试
    ai_response=response.choices[0].message.content
    print("<--------- 大模型返回的结果：",ai_response)
    # 在助手的消息气泡中显示大模型返回的回答
    st.chat_message("assistant").write(ai_response)

    # !!将大模型的回答添加到session_state的历史消息列表中
    st.session_state.messages.append({"role": "assistant", "content": ai_response})
