import json


def JSONWrite(filename, data):

    with open(filename, 'w') as outfile:
        json.dump(data, outfile, indent=4)

def JSONRead(filename):
    data = {}
    try:
        with open(filename) as json_file:
            return json.load(json_file)
    except FileNotFoundError:
        JSONWrite(filename,data)
        return data

JSONRead("yum.json")