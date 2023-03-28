import json

with open("src\main/assets\lang\en_us.json", "r") as f:
    data = json.load(f)

test = data["introduction_1"]

print(str(test))