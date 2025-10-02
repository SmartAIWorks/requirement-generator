

from fastapi import FastAPI

from app.api import stories



app = FastAPI()

app.include_router(stories.router)



@app.get("/")
def root():
    return {"message": "API is running"}