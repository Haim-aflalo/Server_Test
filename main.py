from fastapi import FastAPI, HTTPException
import uvicorn
from pydantic import BaseModel
import json
import string


class Body(BaseModel):
    message: str
    offset: int


def load_endpoints():
    with open("endpoints_data.json") as json_file:
        data = json.load(json_file)
        return data


def load_summary():
    with open("summary.json") as json_file:
        data = json.load(json_file)
        return data


def update_endpoint(data):
    with open("endpoints_data.json", "w") as json_file:
        json.dump(data, json_file)
        return "endpoint file updated"


def update_summary(data):
    with open("summary.json", "w") as json_file:
        json.dump(data, json_file)
        return "summary file updated"


app = FastAPI()


@app.get("/fence/encrypt/")
def fence_crypt(word):
    data = load_endpoints()
    for i in data:
        if i["method"] == "GET" and i["url"] == "/fence/encrypt/":
            i["total_requests_received"] += 1
    update_endpoint(data)
    letters = list(word)
    crypt_word = ""
    for i in letters:
        if i == " ":
            letters.remove(i)
    for i in range(0, len(letters), 2):
        crypt_word += letters[i]
    for j in range(1, len(letters), 2):
        crypt_word += letters[j]
    return crypt_word


@app.post("/fence/decrypt/")
def fence_decrypt(word):
    data = load_endpoints()
    for i in data:
        if i["method"] == "POST" and i["url"] == "/fence/decrypt/":
            i["total_requests_received"] += 1
    update_endpoint(data)
    decrypt_word = ""
    letters = list(word)
    a = letters[len(letters) // 2:]
    b = letters[:len(letters) // 2]
    for i in a:
        for j in b:
            decrypt_word += i
            decrypt_word += j
            a.remove(i)
            b.remove(j)
        continue
    return decrypt_word




@app.get("/cesar/encrypt/")
def cesar_crypt(word,offset):
    data = load_endpoints()
    for i in data:
        if i["method"] == "GET" and i["url"] == "/cesar/encrypt/":
            i["total_requests_received"] += 1
    update_endpoint(data)
    crypted_word = ""
    alphabet = list(string.ascii_lowercase)
    letters_word = list(word)
    for i in range(len(alphabet)):
        for j in letters_word:
            if j == " ":
                crypted_word += j
            if alphabet[i] == j.lower():
                crypted_word += alphabet[(i +offset) % 26]
    return crypted_word


@app.post("/cesar/decrypt/")
def cesar_decrypt(word, offset):
    data = load_endpoints()
    for i in data:
        if i["method"] == "POST" and i["url"] == "/cesar/decrypt/":
            i["total_requests_received"] += 1
    update_endpoint(data)
    crypted_word = ""
    alphabet = list(string.ascii_lowercase)
    letters_word = list(word)
    for i in range(len(alphabet)):
        for j in letters_word:
            if j == " ":
                crypted_word += j
            if alphabet[i] == j.lower():
                crypted_word += alphabet[(i + offset) % 26]
    return crypted_word


