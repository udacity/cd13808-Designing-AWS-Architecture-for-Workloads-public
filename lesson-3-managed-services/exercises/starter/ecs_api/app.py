# fastapi_app.py

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello, World!"}

# TODO: Add Dockerfile for containerizing the application
# TODO: Configure the application to read environment variables for configuration
# TODO: Set up logging for production use