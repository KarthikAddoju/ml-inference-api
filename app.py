from fastapi import FastAPI
from api.routes import router

app = FastAPI(title="ML Inference API")

app.include_router(router)

@app.get("/")
def health_check():
    return {"status": "ML Inference API is running"}
