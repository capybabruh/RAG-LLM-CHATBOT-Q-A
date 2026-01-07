# app.py
import streamlit as st
from rag import get_answer 

st.set_page_config(page_title="Hỏi đáp Đào tạo Toán Tin")

st.title("Trợ lý Sinh viên Toán Tin")
st.caption("Hỏi đáp về chương trình đào tạo, quy chế, học phần")

# Khởi tạo lịch sử chat
if "messages" not in st.session_state:
    st.session_state.messages = []

# Hiển thị lịch sử chat
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Xử lý input
if prompt := st.chat_input("Nhập thắc mắc của bạn:"):
    # 1. Hiển thị câu hỏi User
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # 2. Hiển thị câu trả lời Bot
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        
        with st.spinner("Đang tra cứu quy chế"):
            try:
                # Gọi hàm từ file rag_engine
                full_response = get_answer(prompt)
                
                # Hiệu ứng gõ chữ (optional)
                message_placeholder.markdown(full_response)
            except Exception as e:
                full_response = f"Có lỗi xảy ra: {str(e)}"
                message_placeholder.error(full_response)
        
        # Lưu vào lịch sử
        st.session_state.messages.append({"role": "assistant", "content": full_response})