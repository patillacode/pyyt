import os
import pathlib
import sys

import yt_dlp

from pyfiglet import Figlet
from simple_term_menu import TerminalMenu
from termcolor import colored


def menu(selectable_items: list) -> list:
    """
    Display a terminal menu and allow the user to select multiple items.

    Args:
        selectable_items (list): The list of items to display in the menu.

    Returns:
        list: The list of selected items.
    """
    try:
        terminal_menu: TerminalMenu = TerminalMenu(
            selectable_items,
            multi_select=False,
            show_multi_select_hint=False,
        )
        terminal_menu.show()
        return terminal_menu.chosen_menu_index
    except TypeError:
        raise (KeyboardInterrupt)


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


def welcome() -> None:
    """
    Display a welcome message and banner.
    """
    os.system("clear")
    # lean isometric poison alligator
    fig: Figlet = Figlet(font="larry3d")
    banner: str = colored(fig.renderText(" PYYT "), "cyan")
    print(banner)
    print()
