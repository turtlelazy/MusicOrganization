class Track:
    moodList = []
    id = ""
    def __init__(self, moodList, id):
        if type(moodList) != type(['list']):
            raise Exception ("Error: parameter not a list")

        if len(moodList) != 6:
            raise Exception("Error: parameter not a list of proper length")

        if type(id) != type('str'):
            raise Exception("Error: parameter not a string")

        self.moodList = moodList
        self.id = id

def tempoOnScale(tempo):
    tempoDivScale = tempo/30

    return tempoDivScale * 0.2

def weightedEnergy(track):
    return track.moodList[0] * track.moodList[1] * tempoOnScale(track.moodList[2])
