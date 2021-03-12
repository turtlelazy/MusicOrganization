import os

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

scopes = ["https://www.googleapis.com/auth/youtubepartner"]


def main():
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "client_secret_896189918973-0ph3vd8vrdm82cnl8ggrdu8mt7dd42s3.apps.googleusercontent.com.json"

    # Get credentials and create an API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
    credentials = flow.run_console()
    youtube = googleapiclient.discovery.build(api_service_name,
                                              api_version,
                                              credentials=credentials)

    print(videoTitleAndID("test",youtube))

def videoTitleAndID(searchQuery, youtube):
    request = youtube.search().list(part = 'snippet', q = searchQuery,maxResults=1)
    response = request.execute()
    videoID = response["items"][0]["id"]["videoId"]
    videoTitle = response["items"][0]["snippet"]["title"]
    return {"ID":videoID,"title":videoTitle}

def createPlaylist(title, youtube):
    request = youtube.playlists().insert(part="snippet,status",
                                         body={
                                             "snippet": {
                                                 "title": title
                                             },
                                             "status": {
                                                 "privacyStatus": "unlisted"
                                             }
                                         })
    response = request.execute()
    return response["id"]


if __name__ == "__main__":
    main()