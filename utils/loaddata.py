import json

def loaddata():
    with open("data/data.json", "r") as f:
        content = json.load(f)
    usercontent = [content['users']][0]
    print(usercontent)

loaddata()