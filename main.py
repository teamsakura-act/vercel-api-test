from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()

# CORSを回避するために追加
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
async def search_countryflag(base64data: str):  
    return {"errorMessage": "errorTest", "code": "testCode", "name": "testName", "status": "0"}

@app.get("/population/")
async def scraping_population(countryCode: str, countryName: str):  
    return {"errorMessage": "errorTest", "status": "0", "population": "テスト人"}