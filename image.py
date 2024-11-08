category = "convenience store"

from openai import OpenAI
from dotenv import load_dotenv
import os
from IPython.display import display, Image

# .env 파일에서 환경 변수를 불러오기
load_dotenv()

# 환경 변수에서 API 키 가져오기
api_key = os.getenv("OPENAI_API_KEY")

# OpenAI API 사용 설정
client = OpenAI(api_key=api_key)

# OpenAI API 요청
RESPONSE = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {
            "role": "system",
            "content": f"{category}에 자주 가는 사람에게 어울리는 문장을 동물을 사용하여 재치있게 만들어줘. 당신은 ~한 (동물) 입니다. 이런식으로 만들어봐. 이모지도 넣어줘",
        },
        {
            "role": "user",
            "content": (
                "give prompt in korean"
            )
        }
    ],
    max_tokens=200,
    temperature=1.0,
)

# 객체의 속성으로 content에 접근
prompt = RESPONSE.choices[0].message.content
print(prompt)

# 영어 버전을 DALL-E에 넣을 prompt_input으로 설정
prompt_input = prompt + f" You are the best creator of cartoon character, I want a 3D and like Disney style."

# DALL-E3 이미지 생성
response = client.images.generate(
        model="dall-e-3",
        prompt=prompt_input,
        size="1024x1024",
        quality="hd",  
        n=1,
    )

image_url = response.data[0].url
print(image_url)

# 이미지 표시 및 출력
# display(Image(url=image_url))