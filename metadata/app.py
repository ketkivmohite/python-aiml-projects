import streamlit as st
from PIL import Image
import io

def remove_metadata(image_file):
    img = Image.open(image_file)
    data = list(img.getdata())
    new_img = Image.new(img.mode, img.size)
    new_img.putdata(data)
    return new_img

st.title("Image Metadata Remover")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    cleaned_image = remove_metadata(uploaded_file)
    st.image(cleaned_image, caption="Image with metadata removed", use_column_width=True)

    buf = io.BytesIO()
    cleaned_image.save(buf, format="JPEG")
    byte_im = buf.getvalue()

    st.download_button(
        label="Download Metadata-free Image",
        data=byte_im,
        file_name="image_no_metadata.jpg",
        mime="image/jpeg"
    )
