import os
import pathlib
import sys
from typing import List

import yt_dlp

from pyfiglet import Figlet
from simple_term_menu import TerminalMenu
from termcolor import colored


def menu(selectable_items: List[str]) -> int:
    """
    Display a terminal menu and allow the user to select an item.

    Args:
        selectable_items (List[str]): The list of items to display in the menu.

    Returns:
        int: The index of the selected item.
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
        raise KeyboardInterrupt


def get_video_entries(playlist_url: str) -> List[dict]:
    """
    Get the video entries from a YouTube playlist URL.

    Args:
        playlist_url (str): The URL of the YouTube playlist.

    Returns:
        List[dict]: A list of video entries.
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


def download_and_metadata(video_url: str) -> None:
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
