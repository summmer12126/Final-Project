from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"msg " : "Hello gdsc" }


@app.get("/home")
def home():
    return {"msg" : "mlops study"}


@app.post("/upload")
async def upload(file: UploadFile, directory:str):
    if directory not in directories:
        raise HTTPException(status_code=400, detail="유효하지 않는 디렉토리에요")
    
    
