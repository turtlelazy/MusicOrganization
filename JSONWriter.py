import json
def JSONLoad(filename,encoding):
    file = open(filename, encoding=encoding)
    data = json.load(file)
    file.close()
    return data


print(JSONLoad("TestFiles/Playlist1.json", "utf-8")["playlists"][0])
