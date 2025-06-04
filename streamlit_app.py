import streamlit as st
from llama_index.readers.file import PyMuPDFReader
import os

# 페이지 기본 설정
st.set_page_config(page_title="📄 PDF 업로드", layout="centered")

st.title("📄 법령 PDF 문서 업로드 및 미리보기")

# 파일 업로드 받기
uploaded_file = st.file_uploader("📂 PDF 파일을 업로드하세요", type=["pdf"])

if uploaded_file is not None:
    # 파일 저장 위치 (임시 디렉토리)
    os.makedirs("/tmp", exist_ok=True)
    file_path = os.path.join("/tmp", uploaded_file.name)

    # 업로드된 PDF 파일 저장
    with open(file_path, "wb") as f:
        f.write(uploaded_file.read())

    st.success("✅ PDF 업로드 및 저장 완료")

    # llama-index의 PyMuPDFReader로 문서 로드
    reader = PyMuPDFReader()
    documents = reader.load(file_path=file_path)

    # 첫 페이지 일부 출력
    st.markdown("### 📄 첫 페이지 내용 미리보기:")
    st.write(documents[0].text[:1000])  # 1000자까지 출력

    # 전체 페이지 수 출력
    st.info(f"📃 총 {len(documents)} 페이지 문서를 불러왔습니다.")

    # 세션에 저장해두기 (추후 벡터 인덱싱용)
    st.session_state["uploaded_documents"] = documents
