ydl_opts = {
    "format": "bestaudio/best",
    "postprocessors": [
        {
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192",
        },
    ],
    "outtmpl": f"{get_download_folder()}/%(title)s.%(ext)s",
    "ignoreerrors": True,
    "quiet": False,
    "sleep_interval": 2,
}
