from SpFunctions import *
import sys

arguments = len(sys.argv) - 1

playlist_uri = ""
mode = ""
reverse = False
playlist_name = ""
threshold = 0

if(arguments == 4):
    playlist_uri = sys.argv[1]
    mode = int(sys.argv[2])
    reverse = sys.argv[3].lower() == "true"
    threshold = float(sys.argv[4])
    playlist_name = sp.playlist(playlist_uri)["name"] + str(mode) + str(
        reverse)

elif (arguments == 5):
    playlist_uri = sys.argv[1]
    mode = int(sys.argv[2])
    reverse = sys.argv[3].lower() == "true"
    threshold = float(sys.argv[4])
    playlist_name = sys.argv[5]



elif (arguments == 3):
    playlist_uri = sys.argv[1]
    mode = int(sys.argv[2])
    reverse = sys.argv[3].lower() == "true"
    playlist_name = sp.playlist(playlist_uri)["name"] + str(mode) + str(reverse)

else:
    print("Do you want to select from your playlists? If not enter n")
    choice = input("y/n")
    if(choice == "y"):
        playlists = retrieveUserPlaylistsAsUri()
        if(choice.lower() == "y"):
            for i in range(len(playlists)):
                print("["+str(i)+"]",playlists[i][0])
            index = int(input("Input index of playlist"))
            playlist_uri = playlists[index][1]
            playlist_name = playlists[index][0]
    else:
        playlist_uri = input("Enter URI of playlist")
        playlist_name = sp.playlist(playlist_uri)["name"]

    print("How do you want to order your playlist?")
    print("[0]Energetic\n[1]Positive Vibes\n")
    mode = int(input("Input index of choice."))

    print("Do you want it to descend in that attribute (from big to small)? true/false")
    choice = input("true/false")
    reverse = choice.lower() == "true"

    choice = input("Type in the desired name of the playlist")
    if choice == "":
        playlist_name += str(mode) + str(reverse)
    else:
        playlist_name = choice




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

for track in tracks_list:
    print(track.moodList[mode])
    if track.moodList[mode] < threshold:
        tracks_list.remove(track)

sortTrackAttribute(tracks_list,reverse,mode)

createPlaylistFromTrackObjects(tracks_list,playlist_name)