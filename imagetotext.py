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

        if not texts == []:
            if len(texts[0].description) > 4000:
                text_to_summarize = texts[0].description
                while len(text_to_summarize) > 0:
                    chunk = text_to_summarize[:4000]  # 4000자씩 잘라냅니다.
                    text_to_summarize = text_to_summarize[4000:]  # 처리한 부분을 제외한 나머지 문자열을 얻습니다.
                    summary = gpt_summary(chunk)  # gpt_summary 함수를 호출하여 요약을 생성합니다.
                    image_texts.append(summary)
            else:
                # 문자열 길이가 4000 이하인 경우 그대로 처리
                image_texts.append(gpt_summary(texts[0].description))


    # 에러 처리
    if response.error.message:
        raise Exception(
            "{}\nFor more info on error messages, check: "
            "https://cloud.google.com/apis/design/errors".format(response.error.message)
        )
    return image_texts

