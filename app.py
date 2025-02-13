from io import BytesIO
import os
import requests
import streamlit as st
from together import Together


# Initialize Together client
client = Together(api_key="d14eb566adc1299d8154051505c71486b320e8057a0f06e07dbaf7333c0903d5")

st.title("AI Image Generator 🖼️")
st.write("Enter a prompt to generate an AI-generated image.")

# User input
prompt = st.text_input("Enter your prompt:", "A futuristic city skyline at sunset")

if st.button("Generate Image"):
    if prompt:
        with st.spinner("Generating image... ⏳"):
            try:
                # Make the API call for image generation
                response = client.images.generate(
                    prompt=prompt,
                    model="black-forest-labs/FLUX.1-schnell-Free",
                    steps=4,
                    n=4
                )
                if(response.data):
                    image_url = response.data[0].url  
                    # Display the generated image
                    st.image(image_url, caption="Generated Image", use_container_width=True)

                else:
                    st.error("No image found.")


            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.error("Please enter a prompt to generate an image.")