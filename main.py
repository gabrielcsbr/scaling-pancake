import random

from fastapi import FastAPI

app = FastAPI()


# 127.0.0.1:8000/
@app.get("/helloworld")
async def root():
    return {"message": "Hello World"}


@app.get('/funcaoteste')
async def funcaoteste():
    return {'teste': True, 'num_aleatorio': random.randint(0, 20000)}