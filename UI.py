import streamlit as st
import requests

# Page configuration
st.set_page_config(page_title="Coffee Shop Assistant", page_icon="☕", layout="centered")

st.title("☕ Chatbot Tư vấn")
st.markdown("Xin chào! Bạn muốn dùng cà phê đậm đà, trà trái cây thanh mát hay cần tôi gợi ý đồ uống cho ngày hôm nay?")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Render previous chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("VD: Cho mình hỏi cà phê muối giá bao nhiêu? Có ship không?"):
    
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        
        try:
            # GỌI API VỚI STREAM=TRUE
            response = requests.post(
                "http://127.0.0.1:8000/chat",
                json={"query": prompt, "stream": True}, 
                stream=True 
            )
            
            if response.status_code == 200:
                # Đọc dữ liệu dạng stream, KHÔNG DÙNG .json().get() nữa
                for chunk in response.iter_content(chunk_size=1024):
                    if chunk:
                        text_chunk = chunk.decode("utf-8")
                        full_response += text_chunk
                        message_placeholder.markdown(full_response + "▌")
                
                message_placeholder.markdown(full_response)
            else:
                full_response = f"⚠️ API Error: {response.status_code} - {response.text}"
                message_placeholder.markdown(full_response)
                
        except Exception as e:
            full_response = f"❌ Unable to connect to the backend. Error: {e}"
            message_placeholder.markdown(full_response)
        
        st.session_state.messages.append({"role": "assistant", "content": full_response})