from MoodCalculations import *
import spotipy
from spotipy.oauth2 import SpotifyOAuth

scope = "user-library-read playlist-modify-public user-read-private playlist-read-private"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
user_id = sp.current_user()["id"]

def retrieveUserPlaylistsAsUri():
    dict = []

    playlists = sp.current_user_playlists()
    items = playlists["items"]
    for i in range(len(items)):
        dict.append([items[i]["name"],items[i]["uri"]])
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
        if items[i]["track"]["id"]!=None:
            tracks.append(items[i]["track"]["id"])
    return tracks

def getPlaylistIdAndName(playlist_uri):
    tracks = []

    items = get_playlist_tracks(playlist_uri)
    for i in range(len(items)):
        if items[i]["track"]["id"]!=None:
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
    returnList = []
    trackIdsAndNames = getPlaylistIdAndName(playlist_uri)
    trackIds = []
    for track in trackIdsAndNames:
        trackIds.append(track[0])

    audio_features = []
    length = len(trackIds) // 100
    modulo = len(trackIds) % 100
    for x in range(length):
        tracks = trackIds[x * 100:x * 100 + 100]
        current = sp.audio_features(tracks)
        for audio in current:
            audio_features.append(audio)

    lastTrack = sp.audio_features(trackIds[length * 100:length * 100 + modulo])
    for audio in lastTrack:
        audio_features.append(audio)

    for i in range(len(trackIds)):
        moodList = [
            audio_features[i]["energy"], audio_features[i]["loudness"],
            audio_features[i]["tempo"], audio_features[i]["acousticness"],
            audio_features[i]["valence"], audio_features[i]["danceability"]
        ]

        track = Track(moodList, trackIdsAndNames[i][0], trackIdsAndNames[i][1])
        returnList.append(track)
    return returnList

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
