import pathlib
import sys

import yt_dlp


def get_video_entries(playlist_url):
    """
    Get the video entries from a YouTube playlist URL.

    Args:
        playlist_url (str): The URL of the YouTube playlist.

    Returns:
        list: A list of video entries.
    """
    ydl_opts = {
        "format": "bestaudio/best",
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            },
        ],
        "outtmpl": f"{pathlib.Path().absolute()}/downloads/%(title)s.%(ext)s",
        "extract_flat": "in_playlist",
        "ignoreerrors": True,
        "quiet": False,
        "sleep_interval": 2,
    }
    ydl = yt_dlp.YoutubeDL(ydl_opts)

    results = ydl.extract_info(
        playlist_url,
        download=False,  # We just want to extract the info
    )

    if "entries" in results:
        entries = results["entries"]
        return entries

    print("Something went wrong, no entries in playlist...")
    sys.exit(2)


def download_and_metadata(video_url):
    """
    Download a video as audio and handle metadata.

    Args:
        video_url (str): The URL of the YouTube video.
    """
    # TODO add metadata handling
    ydl_opts = {
        "format": "bestaudio/best",
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            },
        ],
        "outtmpl": f"{pathlib.Path().absolute()}/downloads/%(title)s.%(ext)s",
        "ignoreerrors": True,
        "quiet": False,
        "sleep_interval": 2,
    }
    ydl = yt_dlp.YoutubeDL(ydl_opts)

    ydl.download([video_url])
