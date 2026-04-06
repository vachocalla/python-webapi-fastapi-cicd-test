from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hola Mundo desde K8s y ArgoCD!"}

@app.get("/health")
async def health_check():
    return {"status": "ok"}