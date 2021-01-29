from MoodCalculations import *
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from SpotCredentials import *

scope = "user-library-read playlist-modify-public user-read-private"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
user_id = sp.current_user()["id"]

def retrieveUserPlaylistsAsUri():
    dict = []

    playlists = sp.current_user_playlists()
    items = playlists["items"]
    for i in range(len(items)):
        dict.append(items[i]["uri"])
    return dict


def retrievePlaylistTracksAsName(playlist_uri):
    tracks = []
    items = get_playlist_tracks(playlist_uri)
    for i in range(len(items)):
        tracks.append(items[i]["track"]["name"])

    return tracks


def retrievePlaylistTracksAsId(playlist_uri):
    tracks = []
    items = get_playlist_tracks(playlist_uri)
    for i in range(len(items)):
        tracks.append(items[i]["track"]["id"])

    return tracks

def getPlaylistIdAndName(playlist_uri):
    tracks = []
    items = get_playlist_tracks(playlist_uri)
    for i in range(len(items)):
        tracks.append([items[i]["track"]["id"], items[i]["track"]["name"]])

    return tracks



def get_playlist_tracks(playlist_uri):
    results = sp.playlist_tracks(playlist_uri)
    tracks = results['items']
    while results['next']:
        results = sp.next(results)
        tracks.extend(results['items'])
    return tracks

def createTracksList(playlist_uri):
    trackIds = getPlaylistIdAndName(playlist_uri)
    tracksList = []
    for i in range(len(trackIds)):
        audio_features = sp.audio_features(trackIds[i])[0]
        moodList = [
            audio_features["energy"], audio_features["loudness"],
            audio_features["tempo"], audio_features["acousticness"],
            audio_features["valence"], audio_features["danceability"]
        ]

        track = Track(moodList, trackIds[i][0], trackIds[i][1])
        tracksList.append(track)
    return tracksList

def addTracksToQueue(tracksList):
    for i in range(len(tracksList)):
        sp.add_to_queue(tracksList[i].id)

def createPlaylistFromTrackObjects(tracksObjectList,playlistName):
    trackIdsList = []
    for trackObject in tracksObjectList:
        trackIdsList.append(trackObject.id)
    createPlaylistFromTrack(trackIdsList,playlistName)


def createPlaylistFromTrack(trackIdsList, playlistName):
    tracksLists = []
    length = len(trackIdsList) // 100
    modulo = len(trackIdsList) % 100
    for x in range(length):
        tracks = trackIdsList[x * 100:x * 100 + 100]
        tracksLists.append(tracks)
    lastTrack = trackIdsList[length * 100:length * 100 + modulo]
    tracksLists.append(lastTrack)

    playlist_id = sp.user_playlist_create(user_id, playlistName,
                                          public=True)["uri"]

    for track in tracksLists:
        sp.user_playlist_add_tracks(user_id, playlist_id, track)


def main():


    playlists = retrieveUserPlaylistsAsUri()
    print(playlists)
    '''
    tracksNames = retrievePlaylistTracksAsName(playlists[0])
    tracksList = retrievePlaylistTracksAsId(playlists[0])
    print (tracksList[99],tracksNames[99])
    createPlaylistFromTrack(tracksList,"test")
    '''
    trackStats = createTracksList(playlists[0])
    print(trackStats)
    trackStats.sort(key=lambda x: x.weightedEnergy/2, reverse=False)

    for i in range(len(trackStats)):
        print(trackStats[i].name, trackStats[i].id, trackStats[i].moodList,
              trackStats[i].weightedEnergy)
    print(len(trackStats))
    createPlaylistFromTrackObjects(trackStats,"test")
    



main()