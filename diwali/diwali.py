import streamlit as st
import requests

# Load your Hugging Face token from Streamlit secrets
HF_TOKEN = st.secrets["HF_TOKEN"]
headers = {"Authorization": f"Bearer {HF_TOKEN}"}

st.title(" Free Diwali Greeting Generator (Open Source AI)")
name = st.text_input("Enter the name to wish", "Friend")
theme = st.text_input("Describe Diwali scene for AI image:", "colorful diyas and rangoli")

if st.button("Generate Greeting & Image"):
    # 1. Generate greeting text using Hugging Face Inference API (Zephyr model)
    prompt = f"Write a warm, festive Diwali greeting for {name}."
    response = requests.post(
        "https://api-inference.huggingface.co/models/HuggingFaceH4/zephyr-7b-beta",
        headers=headers,
        json={"inputs": prompt}
    )
    if response.ok and isinstance(response.json(), dict) and 'generated_text' in response.json():
        greeting = response.json()['generated_text']
    elif response.ok and isinstance(response.json(), list) and 'generated_text' in response.json()[0]:
        greeting = response.json()[0]['generated_text']
    else:
        greeting = "Happy Diwali!"

    st.subheader("Your Personalized Diwali Wish")
    st.write(greeting)

    # 2. Generate image using Stable Diffusion (Hugging Face)
    img_prompt = theme + ", Diwali, festival, vibrant, high quality"
    img_response = requests.post(
        "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-2",
        headers=headers,
        json={"inputs": img_prompt}
    )
    if img_response.ok:
        st.subheader("Festive Diwali Image")
        st.image(img_response.content)
    else:
        st.error("Image generation failed. Try again later.")
