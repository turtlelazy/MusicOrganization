from MoodCalculations import *
import spotipy
from spotipy.oauth2 import SpotifyOAuth

scope = "user-library-read"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))


def retrieveUserPlaylistsAsUri():
    dict = []

    playlists = sp.current_user_playlists()
    items = sp.current_user_playlists()["items"]
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


def get_playlist_tracks(playlist_uri):
    results = sp.playlist_tracks(playlist_uri)
    tracks = results['items']
    while results['next']:
        results = sp.next(results)
        tracks.extend(results['items'])
    return tracks

def createTracksList(playlist_uri):
    trackIds = retrievePlaylistTracksAsId(playlist_uri)
    trackStats = []
    for i in range(len(trackIds)):
        audio_features = sp.audio_features(trackIds[i])[0]
        moodList = [
            audio_features["energy"], audio_features["loudness"],
            audio_features["tempo"], audio_features["acousticness"],
            audio_features["valence"], audio_features["danceability"]
        ]

        track = Track(moodList,trackIds[i])
        trackStats.append(track)
    return trackStats

trackStats = createTracksList(playlists[0])
for i in range(len(trackStats)):
    print(trackStats[i].id, trackStats[i].moodList)

def main():
    playlists = retrieveUserPlaylistsAsUri()
    playlist0 = playlists[0]
    print(len(trackStats))

main()