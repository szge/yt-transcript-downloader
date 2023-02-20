# YouTube Transcript Downloader

`yt-transcript-downloader` provides Python functions for downloading YouTube video transcripts into a nice readable format.

## IMPORTANT UPDATE

Big G's new API update killed functionality for getting closed captions for a video unless you are the video owner. Very unfortunate. This project will be abandoned.

## Setup

Follow the [Google YouTube Data API Python Quickstart](https://developers.google.com/youtube/v3/quickstart/python) tutorial, specifically the Prerequisites and Step 1 parts.

Notes: In Step 1 of the quick start tutorial, you will be asked to create an API key and a OAuth 2.0 client ID. Create the OAuth 2.0 client ID with "Desktop app" as the application type. The tutorial says "Other" but it is outdated. Then, in the OAuth consent screen tab, you want to add your account (your Google email or other) as a test user.

Then, create an empty file in the project root directory named `LOGIN_SECRET_FILE.json`.

## Usage

```python
for t in range(5): print(t)
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)

Thanks to [Make a README](https://www.makeareadme.com/).