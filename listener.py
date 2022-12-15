import os
import redis
import gzip


redis_conn = redis.Redis(charset="utf-8", decode_responses=True)
from multiprocessing import Process

def sub(name: str):
    pubsub = redis_conn.pubsub()
    pubsub.subscribe("zlog")
    for message in pubsub.listen():
        if message.get("type") == "message":
            data = message.get("data")
            newdata = gzip.decompress(data).decode('utf-8')
            f = open("output.txt", "a")
            f.write(newdata)
            f.close()
Process(target=sub, args=("reader1a",)).start()
