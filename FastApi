from fastapi import FastAPI
import random

app = FastAPI()

Words=[
    "Hello There",
    "Hello FastAPI",
    "Hello World",
]

@app.get("/random")
def read_random():
    chosen_message = random.choice(Words)
    return {"message": chosen_message}
