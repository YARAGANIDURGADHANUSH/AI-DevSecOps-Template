from fastapi import FastAPI

app = FastAPI(title="AI DevSecOps Template")

@app.get("/")
def home():
    return {"message": "AI DevSecOps Template Running"}

@app.get("/health")
def health():
    return {"status": "healthy"}