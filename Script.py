from SpFunctions import *
import sys

arguments = len(sys.argv) - 1

playlist_uri = ""
mode = ""
reverse = False
playlist_name = "No Name"

if(arguments == 4):
    playlist_uri = sys.argv[1]
    mode = int(sys.argv[2])
    reverse = sys.argv[3].lower() == "true"
    playlist_name = sys.argv[4]

else:
    print("Do you want to select from your playlists? If not enter n")
    choice = input("y/n")
    if(choice.lower() == "y"):
        playlists = retrieveUserPlaylistsAsUri()
        for i in range(len(playlists)):
            print("["+str(i)+"]",playlists[i][0])
        index = int(input("Input index of playlist"))
        playlist_uri = playlists[index][1]

    print("How do you want to order your playlist?")
    print("[0]Energetic\n[1]Positive Vibes\n")
    mode = int(input("Input index of choice."))

    print("Do you want it to descend in that attribute (from big to small)? true/false")
    choice = input("true/false")
    reverse = choice.lower() == "true"

    playlist_name = input("Type in the desired name of the playlist")

if playlist_name == "":
    playlist_name = "Ordered Playlist"


    


def sortTrackAttribute(track,descending,atrIndex):
    track.sort(key=lambda x : x.moodList[atrIndex], reverse = descending)

def sortTrackEnergy(track, descending):
    track.sort(key=lambda x: x.weightedEnergy, reverse=descending)


def sortTrackPositive(track, descending):
    track.sort(key=lambda x: x.weightedHappy, reverse=descending)

def sortTrackPositiveMix(track,descending):
    track.sort(key=lambda x: (x.moodList[4] + x.moodList[5])/2,reverse = descending)

def sortTrackMix(track,descending):
    track.sort(key = lambda x: (x.moodList[0] + x.moodList[4])/2, reverse = descending)

tracks_list = createTracksList(playlist_uri)

if mode == 0:
    sortTrackEnergy(tracks_list, reverse)
elif mode == 1:
    sortTrackPositive(tracks_list, reverse)

createPlaylistFromTrackObjects(tracks_list,playlist_name)