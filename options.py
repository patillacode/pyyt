# Description: This file contains the options for the youtube-dl module.
ydl_opts = {
    "format": "bestaudio/best",
    "postprocessors": [
        {
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192",
        },
    ],
    "ignoreerrors": True,
    "quiet": False,
    "sleep_interval": 2,
}
