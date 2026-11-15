import streamlit as st

st.set_page_config(
    page_title="图书伴读AI",
    page_icon="📖",
    layout="centered"
)

st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #FFE8CC 0%, #FFD2A6 30%, #FFC291 60%, #FFDAB9 100%);
        background-attachment: fixed;
    }
    header {
        background: transparent !important;
    }
    .card {
        background: rgba(255,255,255,0.78);
        border-radius:30px;
        padding:40px;
    }
    h1 {
        color:#7A3E1C;
        text-align:center;
    }
</style>
""", unsafe_allow_html=True)

# 贴纸放在侧边
col1, col2, col3 = st.columns([1,3,1])
with col1:
    st.image("assets/sun.png", width=80)
    st.image("assets/flower.png", width=70)
with col3:
    st.image("assets/rabbit.png", width=80)
    st.image("assets/butterfly.png", width=70)

with col2:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("<h1>✨ 图书伴读AI ✨</h1>", unsafe_allow_html=True)
    st.caption("上传绘本图片，AI为你伴读讲解")
    st.caption("💡 首次打开加载较慢是服务器唤醒中，请稍等～")

    upload_file = st.file_uploader("上传绘本图片", type=["jpg", "png", "jpeg"])
    if upload_file is not None:
        st.image(upload_file, caption="上传的绘本", use_container_width=True)
        if st.button("开始伴读"):
            st.success("AI伴读结果：")
            st.write("这是一个温馨的绘本小故事，画面里有小动物，它正在开心地看风景，我们一起来读一读吧！")
            st.write("📖 导读提示：可以问问小朋友，图里都看到了什么？")
    st.markdown('</div>', unsafe_allow_html=True)
