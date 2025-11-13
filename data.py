import json


class Data:

    @staticmethod
    def load_endpoints():
        with open ("endpoints_data.json") as json_file:
            data = json.load(json_file)
            return data

    @staticmethod
    def load_summary():
        with open("summary.json") as json_file:
            data = json.load(json_file)
            return data


    @staticmethod
    def update_endpoint(data):
        with open("endpoints_data.json","w") as json_file:
            json.dump(data,json_file)
            return "endpoint file updated"

    @staticmethod
    def update_summary(data):
        with open("summary.json","w") as json_file:
            json.dump(data, json_file)
            return "summary file updated"

