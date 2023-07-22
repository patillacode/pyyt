from __future__ import unicode_literals

from termcolor import colored
from simple_term_menu import TerminalMenu
from utils import download_and_metadata, get_video_entries


def main():
    """
    Main function to run the pyyt script.
    """
    welcome_message = colored("Welcome to pyyt - Select your option:\n", "cyan")
    options = [
        colored("Download an entire playlist as audio", "cyan"),
        colored("Download a single video as audio", "cyan"),
    ]

    terminal_menu = TerminalMenu(options, title=welcome_message)
    selected_option_index = terminal_menu.show()

    if selected_option_index == 0:
        playlist_url = input(colored("Please insert the youtube playlist url: ", "cyan"))
        video_entries = get_video_entries(playlist_url)
        video_list = [
            f'https://www.youtube.com/watch?v={video["id"]}' for video in video_entries
        ]
        for video_url in video_list:
            download_and_metadata(video_url)

    elif selected_option_index == 1:
        video_url = input(colored("Please insert the youtube video url: ", "cyan"))
        download_and_metadata(video_url)

    else:
        print(colored("Wrong option. Cya!", "magenta"))


if __name__ == "__main__":
    main()
