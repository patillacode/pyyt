from __future__ import unicode_literals

from simple_term_menu import TerminalMenu
from termcolor import colored

from utils import download_and_metadata, get_video_entries, welcome


def main():
    """
    Main function to run the pyyt script.
    """
    # welcome_message = colored("Welcome to pyyt - Select your option:\n", "cyan")
    options = [
        colored("Download an entire playlist as audio", "cyan"),
        colored("Download a single video as audio", "cyan"),
    ]

    # terminal_menu = TerminalMenu(options, title=welcome_message)
    terminal_menu = TerminalMenu(
        options,
        multi_select=False,
        show_multi_select_hint=False,
    )
    terminal_menu.show()
    selected_option_index = list(terminal_menu.chosen_menu_entries)

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
    welcome()
    main()
