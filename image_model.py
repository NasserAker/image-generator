from together import Together # type: ignore


class image_gen:
    def get_img(prompt):
        client = Together()
        response = client.images.generate(
            prompt,
            model="black-forest-labs/FLUX.1-schnell-Free",
            steps=10,
            n=4
        )
        return(response.data[0].b64_json)

