from fastapi import FastAPI

app = FastAPI(
title = "EarthLens AI"
)

@app.get("/")
def home():
    return {
        "status" : "running",
        "project": "EarthLens AI"
    }