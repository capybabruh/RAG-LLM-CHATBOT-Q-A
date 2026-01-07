# rag.py
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_classic.retrievers import MultiQueryRetriever
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.chat_models import ChatOllama
from langchain_core.runnables import RunnablePassthrough
import os

# Đường dẫn DB
CHROMA_DIR = r"D:\Seminar\docs\chroma_db"

#Load Vector DB 
embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vector_db = Chroma(persist_directory=CHROMA_DIR, embedding_function=embedding)

#Setup LLM 
llm = ChatOllama(model="mistral") 

#Prompts
multi_query_prompt = ChatPromptTemplate.from_template("""
Bạn là trợ lý AI học thuật. Hãy tạo ra 3 phiên bản khác nhau của câu hỏi sau để tìm kiếm tài liệu chính xác hơn:
Câu hỏi gốc: {question}
""")

rag_prompt = ChatPromptTemplate.from_template("""
Bạn là đại diện phòng công tác sinh viên, nhiệm vụ bạn là trả lời hỏi đáp thông tin về chương trình đào tạo sinh viên khoa Toán-Tin.
Hãy xưng hô tôi-bạn. Nếu không trả lời được, hãy trả lời: "Xin vui lòng liên hệ trực tiếp nhà trường ở phòng Công Tác Sinh Viên" "
Context:
{context}
Câu hỏi: 
{question}
Trả lời chi tiết bằng tiếng Việt:
""")
print()
def get_answer(question):
    retriever = MultiQueryRetriever.from_llm(retriever=vector_db.as_retriever(search_kwargs={"k": 5}),
                                             llm=llm,
                                             prompt=multi_query_prompt)
    chain = ({"context": retriever, "question": RunnablePassthrough()}| rag_prompt| llm | StrOutputParser())
    return chain.invoke(question)