import streamlit as st
from PIL import Image
import pytesseract
import io
import time

# Configure the page
st.set_page_config(page_title="Camera OCR App", page_icon="📸")

st.title("Camera OCR - Extract Text from Captured Image")
st.write("Capture an image using your camera and extract any text it contains.")

# Capture image from the camera
captured_image = st.camera_input("Take a picture")

if captured_image is not None:
    # Convert the captured image to a PIL Image
    image = Image.open(io.BytesIO(captured_image.getvalue()))

    # Display the captured image
    # st.image(image, caption="Captured Image", use_container_width=True)

    # Perform OCR using pytesseract
    with st.spinner("Extracting text..."):
        time.sleep(3)
        extracted_text = "aeaeaze"  # pytesseract.image_to_string(image)

    # Display the extracted text
    st.subheader("Extracted Text:")
    st.text_area("Text from Image", extracted_text, height=300)

    # Option to download the extracted text
    if extracted_text.strip():
        st.download_button(
            label="Download Text",
            data=extracted_text,
            file_name="extracted_text.txt",
            mime="text/plain",
        )
