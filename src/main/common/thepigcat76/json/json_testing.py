import json

class component:
    def __init__(self, language):
        with open("src\main/assets\lang/" + language + ".json", "r") as f:
            self.data = json.load(f)
    
    def translatableComponent(self, path):
        rawText = self.data[path]
        text = str(rawText)
        return text