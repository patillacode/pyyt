from __future__ import unicode_literals

import pathlib
import sys

import yt_dlp

ydl_opts = {
    "format": "bestaudio/best",
    "postprocessors": [
        {
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192",
        },
    ],
    "outtmpl": f"{pathlib.Path().absolute()}/downloads/music15/%(artist)s - %(title)s.%(ext)s",
    "extract_flat": "in_playlist",
    "ignoreerrors": True,
    "quiet": False,
    "sleep_interval": 2,
}
ydl = yt_dlp.YoutubeDL(ydl_opts)


def get_video_entries(playlist_url):
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
    # TODO add metadata handling
    ydl.download([video_url])


def main():
    print("Welcome to pyyt - Select your option:\n")
    print("1 - Download an entire playlist as audio\n")
    print("2 - Download a single video as audio\n")

    option = input("Write your selection: ")

    if option == "1":
        playlist_url = input("Please insert the youtube playlist url: ")
        video_entries = get_video_entries(playlist_url)
        video_list = [
            f'https://www.youtube.com/watch?v={video["id"]}' for video in video_entries
        ]
        for video_url in video_list:
            download_and_metadata(video_url)

    elif option == "2":
        video_url = input("Please insert the youtube video url: ")
        download_and_metadata(video_url)

    else:
        print("Wrong option. Cya!")


if __name__ == "__main__":
    main()
