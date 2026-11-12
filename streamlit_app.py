import streamlit as st
import requests

# 页面标题
st.title("图书伴读AI")
st.subheader("上传绘本图片，AI为你伴读讲解")

# 侧边栏
with st.sidebar:
    st.header("设置")
    mode = st.radio("选择模式", ["模拟演示（无后端）", "连接后端"])
    backend_url = st.text_input("后端接口地址", value="http://127.0.0.1:8000/analyze")

# 文件上传
upload_file = st.file_uploader("上传绘本图片", type=["jpg", "png", "jpeg"])

if upload_file is not None:
    st.image(upload_file, caption="上传的绘本", use_container_width=True)

    if st.button("开始伴读"):
        if mode == "模拟演示（无后端）":
            # mock模拟数据，本地调试用
            st.success("AI伴读结果：")
            st.write("这是一个温馨的绘本小故事，画面里有小动物，它正在开心地看风景，我们一起来读一读吧！")
            st.write("📖 导读提示：可以问问小朋友，图里都看到了什么？")
        else:
            # 调用后端
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
