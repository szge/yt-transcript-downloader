import io
import json
import os
import requests
import json
import google.oauth2.credentials
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
from googleapiclient.http import MediaIoBaseDownload

scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]
VIDEO_ID = "4WXs3sKu41I"


def main():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "YOUR_CLIENT_SECRET_FILE.json"
    login_secrets_file = "LOGIN_SECRET_FILE.json"

    try:
        credentials = google.oauth2.credentials.Credentials.from_authorized_user_file(login_secrets_file)
    except ValueError as e:
        # Get credentials and create an API client
        flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
            client_secrets_file, scopes)
        credentials = flow.run_local_server()
        with open(login_secrets_file, "w") as f:
            f.write(credentials.to_json())

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)

    request = youtube.captions().list(part="snippet", videoId=VIDEO_ID)
    response = request.execute()

    # find the English track
    def filter_english_tracks(item):
        # https://developers.google.com/youtube/v3/docs/captions#resource
        # https://developers.google.com/youtube/v3/docs/captions/list
        return item["snippet"]["language"].startswith("en")
    english_track = list(filter(filter_english_tracks, response["items"]))[0]
    print(json.dumps(english_track, indent=4))

    res = requests.get(f'http://video.google.com/timedtext?lang={english_track["snippet"]["language"]}&v={VIDEO_ID}')
    response = json.loads(res.text)
    print(response)


if __name__ == "__main__":
    main()
