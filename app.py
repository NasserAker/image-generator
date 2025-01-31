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

# if st.button("Generate Image"):
#     if prompt:
#         with st.spinner("Generating image... ⏳"):
#             try:
#                 # Make the API call for image generation
#                 response = client.images.generate(
#                     prompt=prompt,
#                     model="black-forest-labs/FLUX.1-schnell-Free",
#                     steps=1,
#                     n=4
#                 )

#                 # Print the response to check its structure
#                 st.write(response)  # This will help you inspect the structure of the response
                
#                 # Assuming the response is a dictionary with a "data" key containing a list of results
#                 if "data" in response and isinstance(response["data"], list) and len(response["data"]) > 0:
#                     image_url = response["data"][0].get("url", None)
                    
#                     if image_url:
#                         # Display the generated image
#                         st.image(image_url, caption="Generated Image", use_column_width=True)

#                         # Optional: Add a download button
#                         img_data = requests.get(image_url).content
#                         st.download_button(
#                             label="Download Image",
#                             data=img_data,
#                             file_name="generated_image.png",
#                             mime="image/png"
#                         )
#                     else:
#                         st.error("No image URL found in the response.")
#                 else:
#                     st.error("Unexpected response format or no data found.")

#             except Exception as e:
#                 st.error(f"Error: {e}")
#     else:
#         st.error("Please enter a prompt to generate an image.")

if st.button("Generate Image"):
    if prompt:
        with st.spinner("Generating image... ⏳"):
            try:
                # Make the API call for image generation
                response = client.images.generate(
                    prompt=prompt,
                    model="black-forest-labs/FLUX.1-schnell-Free",
                    steps=1,
                    n=4
                )

                # Print the response to check its structure
                st.write(response)  # This will help you inspect the structure of the response
                
                # Assuming the response is a dictionary with a "data" key containing a list of results
                if "data" in response and isinstance(response["data"], list) and len(response["data"]) > 0:
                    image_url = response["data"][0].get("url", None)
                    
                    if image_url:
                        # Display the generated image
                        st.image(image_url, caption="Generated Image", use_column_width=True)

                        # Optional: Add a download button
                        img_data = requests.get(image_url).content
                        st.download_button(
                            label="Download Image",
                            data=img_data,
                            file_name="generated_image.png",
                            mime="image/png"
                        )
                    else:
                        st.error("No image URL found in the response.")
                else:
                    st.error("Unexpected response format or no data found.")

            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.error("Please enter a prompt to generate an image.")