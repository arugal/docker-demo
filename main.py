import json
import os
import random
import time

import redis
import uvicorn
from fastapi import FastAPI

app = FastAPI()
r = redis.Redis(host=os.getenv("REDIS_HOST", "127.0.0.1"), port=6379)


@app.get('/app')
@app.post('/app')
async def application():
    time.sleep(random.random())
    obstacle = r.get("obstacle")
    if obstacle is None or obstacle.isspace():
        return "is space"
    return json.loads(obstacle)


@app.get("/read")
async def read():
    with open('obstacle.json', 'r') as obstacle:
        event = json.load(obstacle)
        r.set("obstacle", json.dumps(event))
    return "read"


@app.get("/delete")
async def rm():
    r.delete("obstacle")
    return "deleted"


if __name__ == '__main__':
    # noinspection PyTypeChecker
    uvicorn.run(app, host='0.0.0.0', port=9011)
