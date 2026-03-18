import streamlit as st
from rag_pipeline import process_pdf, get_answer

st.set_page_config(page_title="Endee AI PDF QA", layout="centered")

st.title(" AI PDF Question Answering (Endee + RAG)")

pdf_file = st.file_uploader("Upload PDF", type=["pdf"])

if pdf_file:
    with open("temp.pdf", "wb") as f:
        f.write(pdf_file.read())

    st.success("PDF uploaded successfully!")

    texts = process_pdf("temp.pdf")

    if st.button(" Summarize"):
        if 'texts' in locals():
            st.markdown("### 📝 Summary")

            summary = " ".join(texts[:5])
            st.write(summary[:500])
        else:
            st.warning("Please upload a PDF first.")

    question = st.text_input("Ask your question")

    if st.button("Get Answer"):
        if question:
            answer = get_answer(question)
            st.markdown("### Answer")
            st.write(answer)

    if question:
        st.write("Processing question...")  # DEBUG
        answer = get_answer(question)

        st.markdown("### Answer")
        st.write(answer)