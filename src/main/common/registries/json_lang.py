import json


def translatableComponent(path, language):
    with open("src\main/assets\lang/" + language + ".json", "r") as f:
        data = json.load(f)
    text = str(data[path])
    return text