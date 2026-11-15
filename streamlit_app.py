import streamlit as st

st.set_page_config(
    page_title="图书伴读AI",
    page_icon="📖",
    layout="centered"
)

st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #FFE4C4 0%, #FFD2A6 30%, #FFC291 60%, #FFDAB9 100%);
        background-attachment: fixed;
    }

    header, .css-18e3th9 {
        background: transparent !important;
    }

    .block-container {
        padding-top: 1rem;
        padding-bottom: 1rem;
        max-width: 760px;
        margin: 0 auto;
    }

    .page-wrap {
        position: relative;
        background: rgba(255, 255, 255, 0.25);
        border-radius: 34px;
        padding: 50px 40px;
        margin-top: 20px;
        border: 2px solid rgba(255, 255, 255, 0.65);
        box-shadow: 0 12px 30px rgba(255, 170, 110, 0.25);
    }

    .sticker {
        position: absolute;
        z-index: 2;
        filter: drop-shadow(0 6px 10px rgba(255, 140, 80, 0.25));
    }

    .sticker-sun {
        top: -18px;
        left: -10px;
        width: 110px;
        height: 110px;
    }

    .sticker-book-top {
        top: -24px;
        right: -18px;
        width: 120px;
        height: 100px;
    }

    .sticker-flower {
        bottom: -18px;
        left: -14px;
        width: 100px;
        height: 90px;
    }

    .sticker-cat {
        bottom: -22px;
        right: -10px;
        width: 110px;
        height: 110px;
    }

    .sticker-cloud {
        top: 20px;
        right: 40px;
        width: 70px;
        height: 40px;
        opacity: 0.55;
        z-index: 1;
    }

    .main-card {
        position: relative;
        z-index: 3;
        background: rgba(255, 251, 242, 0.92);
        border-radius: 28px;
        padding: 36px 30px;
        border: 2px solid #FFD7A8;
        box-shadow: inset 0 0 0 4px rgba(255, 255, 255, 0.6);
    }

    h1 {
        color: #7A3E1C;
        font-family: "Comic Sans MS", "微软雅黑", "幼圆", sans-serif;
        text-align: center;
        font-size: 34px;
        margin: 0 0 4px 0;
        letter-spacing: 1px;
    }

    .subtitle {
        text-align: center;
        color: #C26534;
        font-size: 15px;
        margin-bottom: 22px;
    }

    .upload-box {
        background: #FFF7EC;
        border: 2px dashed #FFB35C;
        border-radius: 22px;
        padding: 24px;
    }

    .stButton > button {
        background: linear-gradient(90deg, #FFB35C, #FF7F50);
        color: white;
        border: none;
        border-radius: 24px;
        padding: 12px 32px;
        font-size: 15px;
        font-weight: bold;
        box-shadow: 0 7px 16px rgba(255, 127, 80, 0.32);
        display: block;
        margin: 18px auto 0;
        transition: all 0.2s ease;
    }

    .stButton > button:hover {
        background: linear-gradient(90deg, #FFA43B, #FF6533);
        transform: translateY(-2px);
    }

    .result-box {
        background: #FFF7EC;
        border-left: 5px solid #FFB35C;
        border-radius: 16px;
        padding: 16px 18px;
        margin-top: 18px;
        color: #7A3E1C;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="page-wrap">
    <div class="sticker sticker-sun">< img src="assets/sun.png" alt="sun"></div>
    <div class="sticker sticker-book-top">< img src="assets/book_open.png" alt="book"></div>
    <div class="sticker sticker-flower">< img src="assets/flower.png" alt="flower"></div>
    <div class="sticker sticker-cat">< img src="assets/cat.png" alt="cat"></div>
    <div class="sticker sticker-cloud">< img src="assets/cloud.png" alt="cloud"></div>
    <div class="main-card">
""", unsafe_allow_html=True)

st.markdown("<h1>✨ 图书伴读AI ✨</h1>", unsafe_allow_html=True)
st.markdown('<p class="subtitle">上传绘本图片，AI为你伴读讲解</p >', unsafe_allow_html=True)

st.markdown('<div class="upload-box">', unsafe_allow_html=True)
upload_file = st.file_uploader("上传绘本图片", type=["jpg", "png", "jpeg"])

if upload_file is not None:
    st.image(upload_file, caption="上传的绘本", use_container_width=True)

    if st.button("开始伴读"):
        st.markdown('<div class="result-box">', unsafe_allow_html=True)
        st.success("AI伴读结果：")
        st.write("这是一个温馨的绘本小故事，画面里有小动物，它正在开心地看风景，我们一起来读一读吧！")
        st.write("📖 导读提示：可以问问小朋友，图里都看到了什么？")
        st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</div></div>', unsafe_allow_html=True)
