class Track:
    moodList = []
    id = ""
    name = ""
    weightedEnergy = 0
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
        self.weightedEnergy = energyAlgoStraight(moodList)


def tempoOnScale(tempo):
    tempoDivScale = tempo/30

    return tempoDivScale * 0.2

def energyAlgoStraight(moodList):
    return moodList[0] * moodList[1] * moodList[2]
