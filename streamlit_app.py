import streamlit as st
import requests

st.set_page_config(
    page_title="图书伴读AI",
    page_icon="📖",
    layout="centered"
)

# 贴纸图片地址（后面改成你自己的！）
ASSETS = {
    "sun": "https://raw.githubusercontent.com/你的用户名/你的仓库名/main/assets/sun.png",
    "rainbow": "https://raw.githubusercontent.com/你的用户名/你的仓库名/main/assets/rainbow.png",
    "book_open": "https://raw.githubusercontent.com/你的用户名/你的仓库名/main/assets/book-open.png",
    "book_stack": "https://raw.githubusercontent.com/你的用户名/你的仓库名/main/assets/book-stack.png",
    "flower": "https://raw.githubusercontent.com/你的用户名/你的仓库名/main/assets/flower.png",
    "cat": "https://raw.githubusercontent.com/你的用户名/你的仓库名/main/assets/cat.png",
    "cloud": "https://raw.githubusercontent.com/你的用户名/你的仓库名/main/assets/cloud.png",
    "star": "https://raw.githubusercontent.com/你的用户名/你的仓库名/main/assets/star.png",
}

st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #FFE8CC 0%, #FFD2A6 30%, #FFC291 60%, #FFDAB9 100%);
        background-attachment: fixed;
    }

    header, .css-18e3th9 {
        background: transparent !important;
    }

    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 760px;
        margin: 0 auto;
    }

    h1 {
        color: #7A3E1C;
        font-family: "Comic Sans MS", "微软雅黑", "幼圆", sans-serif;
        text-align: center;
        font-size: 42px;
        margin-bottom: 8px;
        letter-spacing: 1px;
    }

    .subheader-text {
        text-align: center;
        color: #C26534;
        font-size: 18px;
        margin-bottom: 24px;
    }

    .tip-text {
        text-align: center;
        color: #D4864F;
        font-size: 14px;
        margin-bottom: 20px;
    }

    .main-card {
        background: rgba(255, 255, 255, 0.78);
        border-radius: 30px;
        padding: 48px 40px;
        margin: 0 auto;
        position: relative;
        box-shadow: 0 10px 30px rgba(255, 170, 110, 0.25);
        border: 2px solid rgba(255, 255, 255, 0.6);
    }

    .upload-box {
        background: #FFF8EF;
        border: 2px dashed #FFC997;
        border-radius: 22px;
        padding: 30px 20px;
        text-align: center;
        margin-top: 10px;
    }

    .stButton > button {
        background: linear-gradient(90deg, #FFB35C, #FF7F50);
        color: white;
        border: none;
        border-radius: 26px;
        padding: 14px 36px;
        font-size: 16px;
        font-weight: bold;
        box-shadow: 0 8px 18px rgba(255, 127, 80, 0.35);
        display: block;
        margin: 24px auto 0;
        transition: all 0.2s ease;
    }

    .stButton > button:hover {
        background: linear-gradient(90deg, #FFA43B, #FF6533);
        transform: translateY(-2px);
    }

    .css-1d391kg, .stSidebar {
        background: rgba(255, 255, 255, 0.65);
        border-radius: 20px;
        padding: 16px;
    }

    .stImage {
        border-radius: 18px;
        overflow: hidden;
        margin-top: 16px;
    }

    .uploadedFile {
        background: white;
        border-radius: 16px;
        padding: 12px;
    }

    .result-box {
        background: #FFF7EC;
        border-left: 5px solid #FFB35C;
        border-radius: 16px;
        padding: 18px 20px;
        margin-top: 20px;
        color: #7A3E1C;
    }

    /* 统一3D贴纸 */
    .sticker {
        position: fixed;
        z-index: 1;
        opacity: 0.95;
        filter: drop-shadow(0 8px 12px rgba(255, 140, 80, 0.3));
        user-select: none;
        pointer-events: none;
    }

    .sticker img {
        width: 100%;
        height: 100%;
        display: block;
    }

    .sticker-sun {
        top: 90px;
        left: 60px;
        width: 90px;
        height: 90px;
    }

    .sticker-rainbow {
        top: 105px;
        left: 155px;
        width: 100px;
        height: 55px;
    }

    .sticker-book-open {
        top: 115px;
        right: 70px;
        width: 100px;
        height: 75px;
    }

    .sticker-flower {
        bottom: 95px;
        left: 55px;
        width: 80px;
        height: 80px;
    }

    .sticker-cat {
        bottom: 85px;
        right: 95px;
        width: 85px;
        height: 85px;
    }

    .sticker-book-stack {
        bottom: 75px;
        right: 40px;
        width: 75px;
        height: 75px;
    }

    .sticker-cloud {
        top: 60px;
        right: 40px;
        width: 130px;
        height: 75px;
        opacity: 0.4;
        z-index: 0;
    }

    .sticker-star {
        top: 240px;
        left: 14%;
        width: 30px;
        height: 30px;
        opacity: 0.6;
    }
</style>
""", unsafe_allow_html=True)

# 3D贴纸
st.markdown(f'<div class="sticker sticker-sun">< img src="{ASSETS["sun"]}" alt="sun"></div>', unsafe_allow_html=True)
st.markdown(f'<div class="sticker sticker-rainbow">< img src="{ASSETS["rainbow"]}" alt="rainbow"></div>', unsafe_allow_html=True)
st.markdown(f'<div class="sticker sticker-book-open">< img src="{ASSETS["book_open"]}" alt="book-open"></div>', unsafe_allow_html=True)
st.markdown(f'<div class="sticker sticker-flower">< img src="{ASSETS["flower"]}" alt="flower"></div>', unsafe_allow_html=True)
st.markdown(f'<div class="sticker sticker-cat">< img src="{ASSETS["cat"]}" alt="cat"></div>', unsafe_allow_html=True)
st.markdown(f'<div class="sticker sticker-book-stack">< img src="{ASSETS["book_stack"]}" alt="book-stack"></div>', unsafe_allow_html=True)
st.markdown(f'<div class="sticker sticker-cloud">< img src="{ASSETS["cloud"]}" alt="cloud"></div>', unsafe_allow_html=True)
st.markdown(f'<div class="sticker sticker-star">< img src="{ASSETS["star"]}" alt="star"></div>', unsafe_allow_html=True)

# 主体卡片
st.markdown('<div class="main-card">', unsafe_allow_html=True)

st.markdown("<h1>✨ 图书伴读AI ✨</h1>", unsafe_allow_html=True)
st.markdown('<p class="subheader-text">上传绘本图片，AI为你伴读讲解</p >', unsafe_allow_html=True)
st.markdown('<p class="tip-text">💡 首次打开加载较慢是服务器唤醒中，请稍等～</p >', unsafe_allow_html=True)

upload_file = st.file_uploader("上传绘本图片", type=["jpg", "png", "jpeg"])

if upload_file is not None:
    st.image(upload_file, caption="上传的绘本", use_container_width=True)

    if st.button("开始伴读"):
        mode = st.session_state.get("mode", "模拟演示（无后端）")

        if mode == "模拟演示（无后端）":
            st.markdown('<div class="result-box">', unsafe_allow_html=True)
            st.success("AI伴读结果：")
            st.write("这是一个温馨的绘本小故事，画面里有小动物，它正在开心地看风景，我们一起来读一读吧！")
            st.write("📖 导读提示：可以问问小朋友，图里都看到了什么？")
            st.markdown('</div>', unsafe_allow_html=True)
        else:
            backend_url = st.session_state.get("backend_url", "http://127.0.0.1:8000/analyze")
            try:
                res = requests.post(backend_url, files={"file": upload_file})
                if res.status_code == 200:
                    data = res.json()
                    st.markdown('<div class="result-box">', unsafe_allow_html=True)
                    st.success("AI伴读结果：")
                    st.write(data["result"])
                    st.markdown('</div>', unsafe_allow_html=True)
                else:
                    st.error("后端请求失败")
            except Exception as e:
                st.error(f"无法连接后端：{e}")

st.markdown('</div>', unsafe_allow_html=True)

# 侧边栏
with st.sidebar:
    st.header("🎀 设置")
    mode = st.radio("选择模式", ["模拟演示（无后端）", "连接后端"])
    backend_url = st.text_input("后端接口地址", value="http://127.0.0.1:8000/analyze")
    st.session_state["mode"] = mode
    st.session_state["backend_url"] = backend_url
