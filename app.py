import os
import streamlit as st 
from together import Together 


client = Together(api_key="d14eb566adc1299d8154051505c71486b320e8057a0f06e07dbaf7333c0903d5")


st.title("AI Image Generator 🖼️")
st.write("Enter a prompt to generate an AI-generated image.")

# User input
prompt = st.text_input("Enter your prompt:", "A futuristic city skyline at sunset")




# if st.button("Generate Image"):
    # if prompt:
    #     with st.spinner("Generating image... ⏳"):
            # try:
                # response = client.images.generate(
                #     prompt = prompt,
                #     model="black-forest-labs/FLUX.1-schnell-Free",
                #     steps=10,
                #     n=4
                # )
                # image_url = response["data"][0].get("url", None)


                # # Display image
                # st.image(image_url, caption="Generated Image", use_column_width=True)

                # # Download button
                # img_data = requests.get(image_url).content
                # img = Image.open(BytesIO(img_data))
                # st.download_button(
                #     label="Download Image",
                #     data=img_data,
                #     file_name="generated_image.png",
                #     mime="image/png"
                # )

            # except Exception as e:
            #     st.error(f"Error: {e}")



