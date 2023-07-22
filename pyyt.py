from __future__ import unicode_literals

from utils import download_and_metadata, get_video_entries


def main():
    """
    Main function to run the pyyt script.
    """
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
