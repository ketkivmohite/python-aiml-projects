import streamlit as st
import requests
from requests.exceptions import RequestException, Timeout, ConnectionError

# Load your Hugging Face token from Streamlit secrets
try:
    HF_TOKEN = st.secrets["HF_TOKEN"]
    if not HF_TOKEN or HF_TOKEN.strip() == "":
        st.error("Invalid or missing Hugging Face API token. Please configure HF_TOKEN in secrets.")
        st.stop()
except KeyError:
    st.error("Hugging Face API token not found. Please add HF_TOKEN to your Streamlit secrets.")
    st.stop()

headers = {"Authorization": f"Bearer {HF_TOKEN}"}

st.title(" Free Diwali Greeting Generator (Open Source AI)")
name = st.text_input("Enter the name to wish", "Friend")
theme = st.text_input("Describe Diwali scene for AI image:", "colorful diyas and rangoli")

if st.button("Generate Greeting & Image"):
    # 1. Generate greeting text using Hugging Face Inference API (Zephyr model)
    prompt = f"Write a warm, festive Diwali greeting for {name}."
    greeting = None
    
    try:
        response = requests.post(
            "https://api-inference.huggingface.co/models/HuggingFaceH4/zephyr-7b-beta",
            headers=headers,
            json={"inputs": prompt},
            timeout=30
        )
        response.raise_for_status()
        
        # Parse response
        try:
            data = response.json()
            if isinstance(data, dict) and 'generated_text' in data:
                greeting = data['generated_text']
            elif isinstance(data, list) and len(data) > 0 and 'generated_text' in data[0]:
                greeting = data[0]['generated_text']
            elif isinstance(data, dict) and 'error' in data:
                st.warning(f"API returned error: {data['error']}")
                greeting = f"Happy Diwali, {name}! 🪔"
            else:
                st.warning("Unexpected response format from text generation API.")
                greeting = f"Happy Diwali, {name}! 🪔"
        except ValueError:
            st.error("Failed to parse response from text generation API.")
            greeting = f"Happy Diwali, {name}! 🪔"
            
    except Timeout:
        st.error("Text generation request timed out. Please try again.")
        greeting = f"Happy Diwali, {name}! 🪔"
    except ConnectionError:
        st.error("Network connection error. Please check your internet connection.")
        greeting = f"Happy Diwali, {name}! 🪔"
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 429:
            st.error("API rate limit exceeded. Please wait a moment and try again.")
        elif e.response.status_code == 503:
            st.warning("Text generation model is currently loading. Please try again in a moment.")
        elif e.response.status_code == 401:
            st.error("Authentication failed. Please check your API token.")
        else:
            st.error(f"HTTP error occurred: {e.response.status_code}")
        greeting = f"Happy Diwali, {name}! 🪔"
    except RequestException as e:
        st.error(f"Failed to generate greeting: {str(e)}")
        greeting = f"Happy Diwali, {name}! 🪔"

    if greeting:
        st.subheader("Your Personalized Diwali Wish")
        st.write(greeting)

    # 2. Generate image using Stable Diffusion (Hugging Face)
    img_prompt = theme + ", Diwali, festival, vibrant, high quality"
    
    try:
        img_response = requests.post(
            "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-2",
            headers=headers,
            json={"inputs": img_prompt},
            timeout=60
        )
        img_response.raise_for_status()
        
        # Check if response contains image data
        if img_response.content and len(img_response.content) > 0:
            try:
                # Check if response is JSON (error message) or binary (image)
                content_type = img_response.headers.get('content-type', '')
                if 'application/json' in content_type:
                    error_data = img_response.json()
                    if 'error' in error_data:
                        st.warning(f"Image generation API message: {error_data['error']}")
                    else:
                        st.warning("Image generation returned an unexpected response.")
                else:
                    st.subheader("Festive Diwali Image")
                    st.image(img_response.content)
            except ValueError:
                # Not JSON, assume it's image data
                st.subheader("Festive Diwali Image")
                st.image(img_response.content)
        else:
            st.warning("Image generation returned empty content.")
            
    except Timeout:
        st.error("Image generation request timed out. Please try again.")
    except ConnectionError:
        st.error("Network connection error while generating image.")
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 429:
            st.error("API rate limit exceeded for image generation. Please wait and try again.")
        elif e.response.status_code == 503:
            st.warning("Image generation model is currently loading. Please try again in a moment.")
        elif e.response.status_code == 401:
            st.error("Authentication failed for image generation. Please check your API token.")
        else:
            st.error(f"HTTP error occurred during image generation: {e.response.status_code}")
    except RequestException as e:
        st.error(f"Failed to generate image: {str(e)}")
