import os
import io
from google.cloud import vision

def image_text(image_urls):
    # 클라이언트 설정
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'image_service_key.json'
    client_options = {'api_endpoint': 'eu-vision.googleapis.com'}
    client = vision.ImageAnnotatorClient(client_options=client_options)

    file_url = image_urls[0]
    image = vision.Image()
    image.source.image_uri = file_url

    response = client.text_detection(image=image)
    texts = response.text_annotations
    print("Texts:")

    for text in texts:
        print(f'\n"{text.description}"')

        vertices = [
            f"({vertex.x},{vertex.y})" for vertex in text.bounding_poly.vertices
        ]

        print("bounds: {}".format(",".join(vertices)))

    # 에러 처리
    if response.error.message:
        raise Exception(
            "{}\nFor more info on error messages, check: "
            "https://cloud.google.com/apis/design/errors".format(response.error.message)
        )