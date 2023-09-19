import os
from google.cloud import vision
from getgptsummary import gpt_summary

def image_text(image_urls):
    # 클라이언트 설정
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'image_service_key.json'
    client_options = {'api_endpoint': 'eu-vision.googleapis.com'}
    client = vision.ImageAnnotatorClient(client_options=client_options)

    image_texts = []

    for image_url in image_urls:
        file_url = image_url
        image = vision.Image()
        image.source.image_uri = file_url

        response = client.text_detection(image=image)
        texts = response.text_annotations

        image_texts.append(gpt_summary(texts[0].description))

    # 에러 처리
    if response.error.message:
        raise Exception(
            "{}\nFor more info on error messages, check: "
            "https://cloud.google.com/apis/design/errors".format(response.error.message)
        )
    return image_texts

