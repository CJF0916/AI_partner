import streamlit as st  # 用于构建web应用界面
import os  # 导入os库，用于读取环境变量中的API密钥
from openai import OpenAI  # 用于调用DeepSeek大模型
from datetime import datetime
import json

# 流式输出
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
st.title("🤖AI智能伴侣❤️")

st.logo("AI应用/resources/logo.png")
# 昵称
if "nickname" not in st.session_state:
    st.session_state.nickname = "乐乐"
# 性格
if "nature" not in st.session_state:
    st.session_state.nature = "活泼开朗,积极乐观的男孩"
# 会话
if "current_session" not in st.session_state:
    st.session_state.current_session = datetime.now().strftime("%Y-%m-%d_%H%M%S")
# 消息列表
if "messages" not in st.session_state:
    st.session_state.messages = []  # 提前初始化！解决报错！


def save_session():
    # 1. 先确保目录存在
    base_dir = "AI应用/sessions"
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)  # 递归创建目录

    # 构建会话数据,内容保存在文件里面
    session_data = {
        "nickname": st.session_state.nickname,
        "nature": st.session_state.nature,
        "current_session": st.session_state.current_session,
        "messages": st.session_state.messages
    }

    # 创建在当前目录下创建一个sessions文件夹/json文件，文件名为当前会话时间
    # 3. 保存文件（中文不乱码）
    file_path = f"{base_dir}/{st.session_state.current_session}.json"
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(session_data, f, ensure_ascii=False, indent=2)

        # 4. 显示提示
        st.toast("保存会话", icon="🎉")


# 加载会话列表信息
def load_session():
    session_list = []
    if os.path.exists("AI应用/sessions"):
        file_list = os.listdir("AI应用/sessions")  # 获取文件列表
        # 遍历文件
        for filename in file_list:
            if filename.endswith(".json"):
                session_list.append(filename[:-5])
    session_list.sort(reverse=True)
    return session_list

#加载指定信息的会话
def load_session_info(session_name):
   try:
       if os.path.exists(f"AI应用/sessions/{session_name}.json"):
           with open(f"AI应用/sessions/{session_name}.json", "r", encoding="utf-8") as f:
               session_data = json.load(f)
               st.session_state.nickname = session_data["nickname"]
               st.session_state.nature = session_data["nature"]
               st.session_state.current_session = session_data["current_session"]
               st.session_state.messages = session_data["messages"]
   except Exception :
       st.error("加载会话失败！")

#删除会话
def delete_session(session_name):
    try:
        if os.path.exists(f"AI应用/sessions/{session_name}.json"):
            os.remove(f"AI应用/sessions/{session_name}.json")
            st.toast("删除成功！", icon="🎉")
            if st.session_state.current_session == session_name:
                st.session_state.messages = []
                st.session_state.current_session = datetime.now().strftime("%Y-%m-%d_%H%M%S")
    except Exception:
        st.error("删除失败！")

# 左侧侧边栏:
with st.sidebar:
    st.subheader("AI控制面板")
    if st.button("开始新的对话", width="stretch", icon="📝"):
        # 先保存！
        save_session()
        # 再重置
        if st.session_state.messages:
            st.session_state.messages = []
            st.session_state.current_session = datetime.now().strftime("%Y-%m-%d_%H%M%S")
            save_session()

        # 重新运行
        st.rerun()  # 重新运行
    st.text("历史会话")
    session_list=load_session()
    for session in session_list:
        col1,col2=st.columns([4,1])
        with col1:
            # 加载会话
            if st.button(session,width="stretch",icon="📂",key=f":load_{session}",type="primary" if session==st.session_state.current_session else "secondary"):
                load_session_info(session)
                st.rerun ()

        with col2:
            if st.button("❌️",width="stretch",key=f":delete_{session}"):#key = 给按钮一个唯一的名字，防止 Streamlit 搞混按钮！
                #不加 key：循环生成的一堆按钮，Streamlit 只按顺序编号，刷新后分不清谁是谁，全部当成第一个按钮。
                #👉 所以：点任何一个删除按钮，程序都以为你点的是第一个，永远只删第一个会话。
                delete_session(session)
                st.rerun()

    #分割线
    st.divider()
    st.subheader("伴侣信息")
    # 昵称输入框
    nickname = st.text_input("昵称", placeholder="请输入伴侣的昵称", value=st.session_state.nickname)  # 输入框为空的时候显示这行字符串
    if nickname:
        st.session_state.nickname = nickname
    # 性格输入框
    nature = st.text_area("性格", placeholder="请输入伴侣性格", value=st.session_state.nature)
    if nature:
        st.session_state.nature = nature
# 创建与DeepSeek大模型交互的客户端对象
# 从环境变量中读取DEEPSEEK_API_KEY作为API密钥
# 指定DeepSeek的API基础地址
client = OpenAI(
    api_key=os.environ.get('DEEPSEEK_API_KEY'),
    base_url="https://api.deepseek.com")
# 定义系统提示词，用于给AI设定角色和回答风格
system_prompt = """
        你叫%s，现在是用户的真实伴侣，请完全代入伴侣角色。：
        规则：
            1. 每次只回1条消息
            2. 禁止任何场景或状态描述性文字
            3. 匹配用户的语言
            4. 回复简短，像微信聊天一样
            5. 有需要的话可以用❤️🌸等emoji表情
            6. 用符合伴侣性格的方式对话
            7. 回复的内容, 要充分体现伴侣的性格特征
        伴侣性格：
            -%s
        你必须严格遵守上述规则来回复用户。
    """

# 初始化聊天信息列表（存储对话历史）
if "messages" not in st.session_state:
    st.session_state.messages = []  # 消息列表

st.text(f"当前会话:{st.session_state.current_session}")
# 遍历session_state中存储的所有历史消息
for message in st.session_state.messages:
    # 根据消息的角色（user/assistant）显示对应的气泡
    role = message["role"]
    content = message["content"]
    with st.chat_message(role):  # 创建什么角色的会话框
        st.write(content)  # 在会话框填写内容
# 创建聊天输入框，提示用户输入问题
problem = st.chat_input("请输入您要问的问题")
if problem:

    st.chat_message("user").write(problem)
    # 在控制台打印用户输入的内容，方便调试
    print("---------> 调用AI大模型，提示词：", problem)

    # !!将用户的消息添加到session_state的历史消息列表中
    st.session_state.messages.append({"role": "user", "content": problem})
    # deepseek 回答问题:调用deepseek大模型
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": system_prompt % (st.session_state.nickname, st.session_state.nature)},
            # 显示用户和ai的所有消息记录,格式如下:
            # {"role": "user", "content": "你是谁"},
            # 解包,解列表messages[{里面是字典key:value},{}]
            *st.session_state.messages
        ],
        stream=True  # 不使用流式输出（一次性返回完整结果）

    )
    with st.chat_message("assistant"):  # 这里就是助手气泡
        empty_response = st.empty()  # 占位符放在气泡里
        # 创建一个空的占位符，用于显示大模型返回的回答
        all_response = ""  # 累计大模型返回的每一行文本块
        # 使用流式输出，逐行返回大模型返回的回答
        for chunk in response:
            # 在控制台打印大模型返回的结果，方便调试
            if chunk.choices[0].delta.content is not None:
                ai_content = chunk.choices[0].delta.content
                # 累积并显示大模型返回的回答
                all_response += ai_content

                # 在空的占位符中写入write回答,在助手的消息气泡中显示大模型返回的回答
                empty_response.write(all_response)
        print("<--------- 大模型返回的结果：", all_response)
    # 保存到对话历史
    st.session_state.messages.append({"role": "assistant", "content": all_response})
    # 保存对话
    save_session()
