import streamlit as st
import requests

# 页面基础配置
st.set_page_config(
    page_title="图书伴读AI",
    page_icon="📖",
    layout="centered"
)

st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #FFF3E0 0%, #FFE0B2 25%, #FFECB3 50%, #FFD8B8 75%, #FFE9F1 100%);
        background-attachment: fixed;
    }
    header, .css-18e3th9 {
        background: transparent !important;
    }
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    h1 {
        color: #9D4B23;
        font-family: "Comic Sans MS", "微软雅黑", sans-serif;
        text-align: center;
    }
    h2, h3 {
        color: #FF9800;
    }
    .stButton > button {
        background: linear-gradient(90deg, #FFB74D, #FF8A65);
        color: white;
        border: none;
        border-radius: 24px;
        padding: 12px 28px;
        font-weight: bold;
        box-shadow: 0 6px 14px rgba(255, 138, 101, 0.45);
    }
    .stButton > button:hover {
        background: linear-gradient(90deg, #FFA726, #FF7043);
    }
    .css-1d391kg, .stSidebar {
        background: rgba(255, 255, 255, 0.6);
        border-radius: 20px;
        padding: 16px;
    }
    .stImage {
        border-radius: 16px;
        overflow: hidden;
    }
    .uploadedFile {
        background: white;
        border-radius: 16px;
        padding: 12px;
    }
    /* 贴纸定位 */
    .sticker-sun {
        position: fixed;
        top: 120px;
        left: 100px;
        font-size: 60px;
        z-index: 1;
    }
    .sticker-rainbow {
        position: fixed;
        top: 130px;
        left: 170px;
        font-size: 50px;
        z-index: 1;
    }
    .sticker-book1 {
        position: fixed;
        top: 140px;
        right: 100px;
        font-size: 60px;
        z-index: 1;
    }
    .sticker-flower {
        position: fixed;
        bottom: 120px;
        left: 90px;
        font-size: 55px;
        z-index: 1;
    }
    .sticker-cat {
        position: fixed;
        bottom: 100px;
        right: 110px;
        font-size: 60px;
        z-index: 1;
    }
    .sticker-cloud {
        position: fixed;
        top: 80px;
        right: 80px;
        font-size: 70px;
        opacity:0.6;
        z-index: 0;
    }
</style>
""", unsafe_allow_html=True)

# 贴纸
st.markdown('<div class="sticker-sun">🌞</div>', unsafe_allow_html=True)
st.markdown('<div class="sticker-rainbow">🌈</div>', unsafe_allow_html=True)
st.markdown('<div class="sticker-book1">📖</div>', unsafe_allow_html=True)
st.markdown('<div class="sticker-flower">🌼</div>', unsafe_allow_html=True)
st.markdown('<div class="sticker-cat">🐱</div>', unsafe_allow_html=True)
st.markdown('<div class="sticker-cloud">☁️</div>', unsafe_allow_html=True)

# 标题
st.markdown("<h1>✨ 图书伴读AI ✨</h1>", unsafe_allow_html=True)
st.subheader("上传绘本图片，AI为你伴读讲解")
st.markdown("💡 首次打开加载较慢是服务器唤醒中，请稍等～")

# 侧边栏
with st.sidebar:
    st.header("🎀 设置")
    mode = st.radio("选择模式", ["模拟演示（无后端）", "连接后端"])
    backend_url = st.text_input("后端接口地址", value="http://127.0.0.1:8000/analyze")

# 上传
upload_file = st.file_uploader("上传绘本图片", type=["jpg", "png", "jpeg"])

if upload_file is not None:
    st.image(upload_file, caption="上传的绘本", use_container_width=True)
    if st.button("开始伴读"):
        if mode == "模拟演示（无后端）":
            st.success("AI伴读结果：")
            st.write("这是一个温馨的绘本小故事，画面里有小动物，它正在开心地看风景，我们一起来读一读吧！")
            st.write("📖 导读提示：可以问问小朋友，图里都看到了什么？")
        else:
            try:
                res = requests.post(backend_url, files={"file": upload_file})
                if res.status_code == 200:
                    data = res.json()
                    st.success("AI伴读结果：")
                    st.write(data["result"])
                else:
                    st.error("后端请求失败")
            except Exception as e:
                st.error(f"无法连接后端：{e}")
