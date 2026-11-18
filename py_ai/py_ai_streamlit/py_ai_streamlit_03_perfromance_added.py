import streamlit as st
from PIL import Image
from ollama import chat
import time

MODEL_NAME = "moondream"
# MODEL_NAME = "llava"

start_time = time.perf_counter()
st.title("🐕 Define type of dog")

uploaded_file = st.file_uploader("Load photo of dog")

if uploaded_file:
    image = Image.open(uploaded_file)

    st.image(image, caption="Loaded photo")
    with st.spinner("LLaVA is analyzing the image..."):
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

    elapsed_time = time.perf_counter() - start_time
    st.success(f"Dog breed prediction: {prediction}")

    st.info(f"Inference time: {elapsed_time:.2f} seconds")

    print(f"Model: {MODEL_NAME}")
    print(f"Inference time: {elapsed_time:.2f} seconds")
