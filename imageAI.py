import botocore.exceptions
from openai import OpenAI
from fastapi import FastAPI, File, UploadFile, HTTPException
import boto3
import botocore
from dotenv import load_dotenv
import os
import urllib.request
from fastapi.responses import JSONResponse
from typing import Annotated


app = FastAPI()
# client = OpenAI()

# 토큰 정보로드
load_dotenv()


# AWS S3 버킷 사용
AWS_ACCESS_KEY = os.getenv('AccessKeyID')
AWS_SECRET_KEY = os.getenv('SecretAccessKey')
BUCKET_NAME = os.getenv('Region')
AWS_STORAGE_OVERRIDE = True # 기존의 파일을 덮어쓰는 것을 허용할지 여부를 결정
AWS_DEFAULT_REGION = 'ap-northeast-2' # 서울 리전 주소 

#자격 증명 
# s3 클라이언트 생성
def s3_connection():
    try:

        s3_client = boto3.client(
        's3',
        aws_access_key_id=AWS_ACCESS_KEY,
        aws_secret_access_key=AWS_SECRET_KEY,
        region_name=AWS_DEFAULT_REGION,
        )
    except Exception as e:
        print(e)
    else:
        print("s3 bucket connected!")
        return s3_client

s3 = s3_connection()


bucket = BUCKET_NAME
file_name = 'C:/ITStudy/generatedImage/generated_image.jpg' 
key = 'uploads2/test.jpg' 

# @app.post("/files/")
# async def create_file(file: Annotated[bytes, File()]):
#     return {"file_size": len(file)}


@app.post("/uploadfile")
async def create_upload_file():
     s3.upload_file(file_name, bucket, key,
                    ExtraArgs={'ContentType':'image/jpeg'})

# @app.post("/upload")
# async def upload(file:UploadFile, directory:str):
#     file_name = './img.jpg' 
#     key = 'uploads2/test.jpg' 

#     s3_client.upload_file(file_name, bucket, key)
#     # try:
#     #     s3_client.upload_file(file_name, bucket, key)
#     # except (botocore.exceptions.BotoCoreError, botocore.exceptions.ClientError) as e:
#     #     raise HTTPException(status_code=500, detail=f"s3 upload fails: {str(e)}")
    
#     # url = "https://%s.s3.ap-northeast-2.amazonaws.com/%s" % (
#     #     bucket,
#     #     key
#     # )

#     # return JSONResponse(content={"url": url})




# res = s3_client.upload_file(image_url, bucket, key)

# Upload the file




# DALLE-E 3을 사용하면 한 번에 1개의 이미지를 요청 할 수 있음(병렬 요청을 통해 더 많은 이미지를 요청할 수 있음)

# style, prompt 지정
# style = "self-Destructive"
# prompt="a white siamese cat"

# response = client.images.generate(
#     model="dall-e-3",
#     prompt=prompt,
#     size="1024x1024",
#     quality="standard",
#     n=1,
# )

# # 생성된 이미지의 URL을 저장함
# image_url = response.data[0].url
# print(f'img_url : {image_url}')

