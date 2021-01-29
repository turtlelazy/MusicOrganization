class Track:
    moodList = [] #energy,loudness,tempo,acousticness,valence,danceability
    id = ""
    name = ""
    weightedEnergy = 0
    weightedHappy = 0
    def __init__(self, moodList, id, name):
        if type(moodList) != type(['list']):
            raise Exception ("Error: parameter not a list")

        if len(moodList) != 6:
            raise Exception("Error: parameter moodList not a list of proper length")

        if type(id) != type('str'):
            raise Exception("Error: parameter id not a string")

        if type(name) != type('str'):
            raise Exception("Error: parameter name not a string")

        self.moodList = moodList
        self.id = id
        self.name = name
        self.weightedEnergy = energyAlgoBasic(moodList)
        self.weightedHappy = happyAlgoBasic(moodList)


def tempoOnScale(tempo):
    tempoDivScale = tempo/30

    return tempoDivScale * 0.2

def energyAlgoBasic(moodList):
    return moodList[0]

def happyAlgoBasic(moodList):
    return moodList[4]

