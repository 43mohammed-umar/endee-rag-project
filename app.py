import streamlit as st
from rag_pipeline import process_pdf, get_answer

st.title("AI PDF Question Answering (Endee Project)")

# Upload PDF
pdf_file = st.file_uploader("Upload a PDF file", type=["pdf"])

if pdf_file is not None:
    with open("temp.pdf", "wb") as f:
        f.write(pdf_file.read())

    st.success("PDF uploaded successfully!")

    texts = process_pdf("temp.pdf")

    # Summary Feature
    if st.button("📄 Summarize Document"):
        st.markdown("## 📝 Summary")
        st.write(" ".join(texts[:3]))

    # Ask question
    question = st.text_input("Ask a question from the document")

    if question:
        answer = get_answer(question, texts)

        st.markdown("## Answer")
        st.write(answer)