import re
import json

def gen_json():
    dic = {}
    with open("Names.txt", "r+") as text:
        count = 0
        for line in text:
            fullname = re.sub(r"\s+", "_", line.strip()).split("_")
            dic["n" + str(count)] = {
                "name" : fullname[0],
                "surname": fullname[1],
                "id": "n" + str(count),
                "likes": 0,
            }
            count += 1
    with open('names.json', 'w') as json_file:
        json.dump(dic, json_file)

def update_likes(id):
    with open("names.json", "r") as jsonFile:
        data = json.load(jsonFile)
    data[id]["likes"] += 1
    with open("names.json", "w") as jsonFile:
        json.dump(data, jsonFile)

def get_names() -> dict:
    with open("names.json", "r") as jsonFile:
        data = json.load(jsonFile)
    return data

def save(data):
    with open("names.json", "w+") as fp:
        json.dump(data, fp)

gen_json()
