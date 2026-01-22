import streamlit as st
from speech_to_text import transcribe_audio
from summarizer import summarize_text

st.set_page_config(page_title="AI Meeting Assistant")

st.title("🎙️ Real-Time AI Meeting Assistant")
st.write("Upload a WAV audio file to get transcription and summary")

uploaded_file = st.file_uploader("Upload meeting audio (WAV format)", type=["wav"])

if uploaded_file:
    st.info("Processing audio...")

    text = transcribe_audio(uploaded_file)
    st.subheader("📝 Transcription")
    st.write(text)

    summary = summarize_text(text)
    st.subheader("📌 Summary")
    st.write(summary)
