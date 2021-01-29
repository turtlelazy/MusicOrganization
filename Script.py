from SpFunctions import *
import sys


playlists = retrieveUserPlaylistsAsUri()



#print(sp.audio_features(retrievePlaylistTracksAsId(playlist)))
x = createTracksList(playlists[2])
for el in x:
    print (el.moodList, el.id,el.name)

print(len(x))

createPlaylistFromTrackObjects(x,"test")

def sortTrack(track,aspect):
    track.sort(key=lambda x: x.weightedEnergy, reverse=False)
