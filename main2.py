from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def welcome_wagon():
    return {"Hi": "Welcome"}
