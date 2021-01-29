# QueueByMood
This project utilizes the Spotify API to queue a user's Spotify playlist by mood!

How to use:
In order to use this python script, you need to:
    - Have Spotipy installed (if not installed, use pip to install "spotipy")
    - Have access to Spotify Web API (more info here: https://developer.spotify.com/documentation/web-api/quick-start/) 

Before cd'ing into the directory of the python script, run these commands in your terminal. If using a Windows terminal, use "SET" instead of "export"

```
export SPOTIPY_CLIENT_ID='YOURCLIENTIDHERE'
export SPOTIPY_CLIENT_SECRET='YOURCLIENTSECRETHERE'
export SPOTIPY_REDIRECT_URI='http://127.0.0.1:9090'
```