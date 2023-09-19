import os
import openai
from chatgpt_service_key import  gpt_key

openai.api_key = gpt_key

def gpt_summary(content):
    completion = openai.ChatCompletion.create(
        model ="gpt-3.5-turbo",
        messages =[
            {"role" : "system", "content" : "you are a sentence summary robot"},
            {"role": "user", "content": "한국어로 잘 번역해 줄 수 있지?"},
            {"role": "assistant", "content": "당연하죠"},
            {"role":"user", "content" : content}
        ],
        temperature = 0,
        stop=None
    )

    return completion.choices[0].message.content


