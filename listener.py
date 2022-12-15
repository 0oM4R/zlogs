import os
import redis
import gzip
import json

redis_conn = redis.Redis(charset="utf-8", decode_responses=False)
from multiprocessing import Process

def sub(name: str):

    pubsub = redis_conn.pubsub()
    pubsub.subscribe("zlog")
    print("[+] Subscribed....")
    for message in pubsub.listen():
         if message.get("type") == "message":
            data = message.get("data")
            decompressedData =gzip.decompress(data).decode('utf-8')
            f = open("/output.txt", "a")
            f.write(decompressedData)
            f.close()

Process(target=sub, args=("reader",)).start()
