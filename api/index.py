from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello! Your bot is running on Vercel 🚀"}

@app.get("/ping")
def ping():
    return JSONResponse(content={"status": "ok"})
