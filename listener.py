import os
import redis
import gzip
import json
from datetime import datetime
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
            f = open("/zlogOutput.txt", "a")
            current_time=datetime.now()
            f.write("\n ---------------------"+current_time.strftime("%d/%m/%Y %H:%M:%S")+"------------------------\n")
            f.write(decompressedData)
            f.close()

Process(target=sub, args=("reader",)).start()
