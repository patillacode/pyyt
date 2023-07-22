from __future__ import unicode_literals

from termcolor import colored
from utils import download_and_metadata, get_video_entries


def main():
    """
    Main function to run the pyyt script.
    """
    print(colored("Welcome to pyyt - Select your option:\n", "cyan"))
    print(colored("1 - Download an entire playlist as audio\n", "cyan"))
    print(colored("2 - Download a single video as audio\n", "cyan"))

    option = input(colored("Write your selection: ", "cyan"))

    if option == "1":
        playlist_url = input(colored("Please insert the youtube playlist url: ", "cyan"))
        video_entries = get_video_entries(playlist_url)
        video_list = [
            f'https://www.youtube.com/watch?v={video["id"]}' for video in video_entries
        ]
        for video_url in video_list:
            download_and_metadata(video_url)

    elif option == "2":
        video_url = input(colored("Please insert the youtube video url: ", "cyan"))
        download_and_metadata(video_url)

    else:
        print(colored("Wrong option. Cya!", "magenta"))


if __name__ == "__main__":
    main()
