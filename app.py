from io import BytesIO
import os
import requests




from streamlit import st
from together import Together

# Initialize Together client
client = Together(api_key=os.environ.get("TOGETHER_API_KEY"))

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
                    steps=10,
                    n=4
                )

                # Get the first image URL from the response
                image_url = response.get("data", [])[0].get("url", None)
                
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

            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.error("Please enter a prompt to generate an image.")
