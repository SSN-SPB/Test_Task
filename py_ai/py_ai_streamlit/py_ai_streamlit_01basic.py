import streamlit as st
from PIL import Image
from ollama import chat

MODEL_NAME = "llava"

st.title("🐕 Define type of dog")

uploaded_file = st.file_uploader("Load photo of dog")

if uploaded_file:
    image = Image.open(uploaded_file)

    st.image(image, caption="Loaded photo")

    response = chat(
        model=MODEL_NAME,
        messages=[
            {
                "role": "user",
                "content": "Identify the breed of this dog.",
                "images": [uploaded_file.getvalue()],
            }
        ],
    )

    prediction = response.message.content

    st.success(f"Dog breed prediction: {prediction}")
