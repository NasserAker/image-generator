from ast import Import
from io import BytesIO
import os
import requests
import streamlit as st 
from together import Together

client = Together(api_key=os.environ.get("TOGETHER_API_KEY"))

response = client.chat.completions.create(
    model="mistralai/Mixtral-8x7B-Instruct-v0.1",
    messages=[{"role": "user", "content": "tell me about new york"}],
)
print(response.choices[0].message.content)



# st.title("AI Image Generator 🖼️")
# st.write("Enter a prompt to generate an AI-generated image.")

# # User input
# prompt = st.text_input("Enter your prompt:", "A futuristic city skyline at sunset")




# if st.button("Generate Image"):
#     if prompt:
#         with st.spinner("Generating image... ⏳"):
#             try:
#                 response = client.images.generate(
#                     prompt = prompt,
#                     model="black-forest-labs/FLUX.1-schnell-Free",
#                     steps=10,
#                     n=4
#                 )
#                 image_url = response["data"][0].get("url", None)


#                 # Display image
#                 st.image(image_url, caption="Generated Image", use_column_width=True)

#                 # Download button
#                 img_data = requests.get(image_url).content
#                 img = Image.open(BytesIO(img_data))
#                 st.download_button(
#                     label="Download Image",
#                     data=img_data,
#                     file_name="generated_image.png",
#                     mime="image/png"
#                 )

#             except Exception as e:
#                 st.error(f"Error: {e}")



