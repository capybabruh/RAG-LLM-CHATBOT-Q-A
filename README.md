# Trợ lý AI Sinh viên Toán - Tin (RAG Chatbot)

Một hệ thống Hỏi-Đáp (Q&A) thông minh dựa trên kiến trúc RAG (Retrieval-Augmented Generation), được thiết kế để hỗ trợ sinh viên khoa Toán - Tin tra cứu thông tin về chương trình đào tạo, quy chế học vụ và các học phần. 

Hệ thống sử dụng **Mistral OCR** để trích xuất dữ liệu từ PDF, lưu trữ vector với **ChromaDB**, và sử dụng LLM local thông qua **Ollama** để đảm bảo tính bảo mật và phản hồi tự nhiên. Giao diện người dùng được xây dựng bằng **Streamlit**.

##Tính năng chính

- **Trích xuất dữ liệu độ chính xác cao:** Sử dụng API `mistral-ocr-latest` để đọc và số hóa các tài liệu PDF (chương trình đào tạo, quy chế).
- **Tìm kiếm ngữ nghĩa (Semantic Search):** Nhúng (embedding) văn bản bằng model `all-MiniLM-L6-v2` của HuggingFace và lưu trữ tại ChromaDB.
- **Tối ưu hóa câu truy vấn:** Sử dụng `MultiQueryRetriever` của LangChain để tự động tạo ra nhiều phiên bản của câu hỏi, giúp tìm kiếm context chính xác hơn.
- **Local LLM:** Chạy hoàn toàn trên máy cá nhân với model `mistral` qua Ollama, không tốn chi phí API cho việc sinh văn bản (Generation).
- **Giao diện thân thiện:** Web app trực quan, có lưu trữ lịch sử chat được xây dựng bằng Streamlit.

##Tech Stack

- **Framework:** LangChain, Streamlit
- **LLM Engine:** Ollama (Mistral 7B)
- **OCR:** Mistral API
- **Vector Database:** ChromaDB
- **Embeddings:** HuggingFace (`sentence-transformers/all-MiniLM-L6-v2`)

##Cài đặt

### 1. Yêu cầu hệ thống
- Python 3.9+
- [Ollama](https://ollama.com/) đã được cài đặt trên máy.

### 2. Khởi tạo môi trường
Clone repository và cài đặt các thư viện cần thiết:

```bash
git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
cd your-repo-name
pip install -r requirements.txt
