#!/usr/bin/env python3
import requests
import sys
import base64
import logging
import random
import uuid

print(sys.version_info)


def load_accounts():
    with open("twitter-accounts.txt","r") as fd:
        for line in fd:
            yield line.strip()

def gen_garbage(url:str):
    #this is to throw off the analyst
    # after reaching out to twitter, send garbage requests to list of random domains
    if "Serial" in url or "status" in url:
        requests.post(url,headers={"Authorization":"66","Command":base64.b64encode(b"I have a feeling this account might contain the answer.")})
    elif "twitter" not in url:
        nonce = uuid.uuid4()
        requests.post(url,headers={"Authorization":"501","Command":base64.b64encode(str(nonce).encode("utf-8") + b"This is not the twitter account you should be investigating.")})
         
    else:
        nonce = random.randint(1,10000)
        requests.post(url,headers={"Authorization":"501","Command":base64.b64encode(str(nonce).encode("utf-8") + b"This is not the twitter account you should be investigating.")})
    

def pull_feed(url:str):
    resp = requests.get(url)
    if resp.status_code:
        gen_garbage(url)    
    else:
        logging.info(f"request failed {url}")


if __name__ == "__main__":
    for link in load_accounts():
        pull_feed(link)
