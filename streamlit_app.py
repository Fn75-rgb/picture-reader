import streamlit as st
import time

st.set_page_config(page_title="绘本AI伴读", layout="wide")
st.title("纸质绘本AI伴读系统")

upload_img = st.file_uploader("上传绘本照片", type=["jpg", "png", "jpeg"])
user_q = st.text_input("向AI提问（空着就自动讲解这一页）")

if st.button("开始伴读") and upload_img is not None:
    with st.spinner("正在识别、生成讲解、合成语音，请稍等..."):
        time.sleep(1.5)
        mock_data = {
            "code": 0,
            "ocr_text": "小兔子在草地上开心地放风筝。风吹呀吹，风筝飞得高高的。",
            "ai_reply": "小朋友你看，小兔子正在放风筝哦！春天的风很适合放风筝，你有没有放过风筝呀？",
            "audio_path": ""
        }
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("📷 原图")
        st.image(upload_img)
    with col2:
        st.subheader("📝 OCR识别文字")
        st.write(mock_data["ocr_text"])
        st.subheader("🤖 AI伴读讲解")
        st.write(mock_data["ai_reply"])
        st.subheader("🔊 语音朗读")
        st.info("等后端完成后，这里会播放语音")

if st.button("清空"):
    st.rerun()
