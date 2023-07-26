from __future__ import unicode_literals

import sys
import traceback

from termcolor import colored

from .utils import download_and_metadata, get_video_entries, menu, welcome


def main() -> None:
    """
    Main function to run the pyyt script.
    """
    print(colored("Select your option:", "cyan"))
    options = [
        "Download an entire playlist as audio",
        "Download a single video as audio",
    ]
    selected_option = menu(options)

    if selected_option == 0:
        playlist_url = input(
            colored("Please insert the YouTube playlist URL: ", "magenta")
        )
        video_entries = get_video_entries(playlist_url)
        video_list = [
            f'https://www.youtube.com/watch?v={video["id"]}' for video in video_entries
        ]
        for video_url in video_list:
            download_and_metadata(video_url)

    elif selected_option == 1:
        video_url = input(colored("Please insert the YouTube video URL: ", "magenta"))
        download_and_metadata(video_url)

    else:
        print(colored("Wrong option. Cya!", "magenta"))


if __name__ == "__main__":
    welcome()
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()

    except Exception as err:
        print(traceback.format_exc())
        print("\n", err, "\n")
