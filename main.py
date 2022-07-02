import random
import time

import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get('/artist')
@app.post('/artist')
async def application():
    time.sleep(random.random())
    return {'artist': 'Luis Fonsi'}


if __name__ == '__main__':
    # noinspection PyTypeChecker
    uvicorn.run(app, host='0.0.0.0', port=9011)