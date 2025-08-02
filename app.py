
import streamlit as st
from huggingface_hub import InferenceClient

st.title("🎤 Text-to-Speech Generator")

API_KEY = "hf_your_actual_token_here"  # <-- Replace this with your Hugging Face token
client = InferenceClient(provider="fal-ai", api_key=API_KEY)

text = st.text_area("Enter your text:", "Welcome to EchoVerse!")
model = st.selectbox("Choose a model", [
    "ResembleAI/chatterbox",
    "espnet/kan-bayashi_ljspeech_vits",
    "facebook/mms-tts-eng"
])

if st.button("Generate Audio"):
    with st.spinner("Generating..."):
        audio = client.text_to_speech(text, model=model)
        st.audio(audio, format="audio/wav")
        st.download_button("⬇️ Download Audio", data=audio, file_name="output.wav")
