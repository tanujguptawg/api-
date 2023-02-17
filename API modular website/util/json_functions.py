import json


class JsonClass:
    def __init__(self, filepath):
        self.filepath = filepath

    @staticmethod
    def read_json(filepath):
        with open(filepath, 'r', encoding="utf-8") as file:
            data = json.load(file)

        return data

    @staticmethod
    def write_data(filepath, data):
        with open(filepath, 'w', encoding="utf-8") as fp:
            json.dump(data, fp, indent=4)
