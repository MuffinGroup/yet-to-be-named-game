import json

with open("src\main/assets\lang/test.json", "r") as f:
    data = json.load(f)
    f.close()  # NOTE: closed buffer even though not needed - just a habit.
