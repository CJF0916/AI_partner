import streamlit as st
#页面布局
st.set_page_config(
    page_title="AI-stream",
    page_icon="🧊",
    layout="centered",
    initial_sidebar_state="expanded",#侧边栏
    menu_items={#菜单
        'About': "# hello python!"
    }
)
# 标题
st.title("AI智能伴侣")
# 段落
st.write("布偶猫是一种源于美国的大型半长毛猫，以温顺黏人的“小狗猫”性格、湛蓝色的眼睛和松弛柔软的抱感著称，拥有重点色、手套色和双色等经典图案，"
         "需要定期梳毛并注意遗传性心脏病等健康问题，是理想的家庭陪伴宠物。")
# 图片
st.image("D://logo.jpg")
# 分隔线
st.divider()
# 表格
data = {"姓名": ["王林", "李慕婉", "贝罗", "莫厉海", "石萧", "红蝶", "十三"],
        "学号": ["20230001", "20230002", "20230003", "20230004", "20230005", "20230006", "20230007"],
        "语文": [80, 90, 85, 70, 95, 90, 85],
        "数学": [87, 92, 87, 81, 92, 69, 83],
        "英语": [90, 85, 90, 95, 80, 85, 90],
        "总分": [257, 267, 262, 241, 267, 244, 258]}
st.table(data)

# ===================== 全部注释！避免报错 =====================
st.video("AI应用/resources/news.mp4")
st.audio("AI应用/resources/news.mp3")
st.logo("AI应用/resources/logo.png")
st.image("AI应用/resources/cat.jpg")
# ==============================================================
# 输入框
name = st.text_input("请输入你的姓名：")

if name:
    st.write("你好, ", name)


# 密码
password = st.text_input("请输入你的密码：", type="password")

if password:
    st.write(f"你的密码是{password}吗?")

age = st.number_input('年龄：')

st.write(f'你输入的年龄是{age}岁')

checked = st.checkbox("同意以上条款")
if checked:
  st.write("同意")
else:
  st.write("不同意")

subject = st.selectbox(
  "意向学科",
  [
    "AI大模型开发",
    "AI智能应用开发",
    "AI嵌入式+机器人开发",
    "AI测试",
    "AI运维"
  ]
)

st.write(f"你喜欢{subject }")
submitted = st.button("新建会话")

if submitted:
  st.write(f"新建会话成功啦")

# 用户信息
with st.chat_message("user"):
    st.write("Hello 👋")

# 机器人信息
message = st.chat_message("assistant")
message.write("Hello human")