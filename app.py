from google.cloud import translate_v2 as translate
import streamlit as st

# Initialize Google Cloud Translator (Make sure to set up authentication)
translator = translate.Client()

# Streamlit app title
st.title("Kannada to English Translator")

# Text input for Kannada
kannada_text = st.text_area("Enter Kannada text here:")

# Translate button
if st.button("Translate"):
    if kannada_text.strip() == "":
        st.warning("Please enter some Kannada text to translate.")
    else:
        # Translate text
        translation = translator.translate(kannada_text, source_language='kn', target_language='en')
        english_text = translation['translatedText']

        # Display the translated English text
        st.write("### Translated English Text:")
        st.write(english_text)
