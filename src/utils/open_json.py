import json


def open_json(dir: str):
    with open(dir) as json_file:
        data = json.load(json_file)
    return data
