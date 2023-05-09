import json

d = {"data": "hello"}

with open("data.json", "w") as f:
    json.dump(d, f)

with open("data.json", "r") as f:
    x = json.load(f)
    print(x)
