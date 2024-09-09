import streamlit as st
from googletrans import Translator

# Initialize the Google Translate API
translator = Translator()

# Streamlit Web App
st.title("Language Translator")

# Language selection
languages = {
    'en': 'English',
    'fr': 'French',
    'es': 'Spanish',
    'de': 'German',
    'hi': 'Hindi',
    'zh-cn': 'Chinese (Simplified)',
    'ja': 'Japanese',
    'ko': 'Korean',
    'it': 'Italian'
}

src_lang = st.selectbox("Select Source Language", list(languages.keys()), format_func=lambda x: languages[x])
tgt_lang = st.selectbox("Select Target Language", list(languages.keys()), format_func=lambda x: languages[x])

# Text input
text = st.text_area("Enter text to translate", "Hello, how are you?")

# Translation button
if st.button("Translate"):
    if text:
        translation = translator.translate(text, src=src_lang, dest=tgt_lang)
        st.write("Translated Text:")
        st.write(translation.text)
    else:
        st.warning("Please enter text to translate.")