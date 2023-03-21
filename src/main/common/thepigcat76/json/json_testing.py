import json

with open("src\main/assets\lang\en_us.json", "r") as f:
    data = json.load(f)

print(data["introduction_welcome"])