import unittest

# from io import StringIO
# from unittest.mock import patch

# from pyyt import main


class TestPyyt(unittest.TestCase):
    pass
    # @patch(
    #     "builtins.input", side_effect=["0", "playlist_url", "n", "1", "video_url", "n"]
    # )
    # def test_main(self, mock_input):
    #     with patch("sys.stdout", new=StringIO()) as fake_output:
    #         main()
    #         output = fake_output.getvalue().strip()
    #         self.assertIn("Select your option:", output)
    #         self.assertIn("Please insert the YouTube playlist URL:", output)
    #         self.assertIn("Please insert the YouTube video URL:", output)
    #         self.assertIn("Wrong option. Cya!", output)

    # @patch("pyyt.get_video_entries")
    # @patch("pyyt.download_and_metadata")
    # def test_main_download_playlist(
    #     self, mock_download_and_metadata, mock_get_video_entries
    # ):
    #     mock_get_video_entries.return_value = [
    #         {"id": "video1"},
    #         {"id": "video2"},
    #         {"id": "video3"},
    #     ]
    #     with patch("builtins.input", side_effect=["0", "playlist_url", "n"]):
    #         main()
    #         mock_download_and_metadata.assert_called_with(
    #             "https://www.youtube.com/watch?v=video1"
    #         )
    #         mock_download_and_metadata.assert_called_with(
    #             "https://www.youtube.com/watch?v=video2"
    #         )
    #         mock_download_and_metadata.assert_called_with(
    #             "https://www.youtube.com/watch?v=video3"
    #         )

    # @patch("pyyt.download_and_metadata")
    # def test_main_download_single_video(self, mock_download_and_metadata):
    #     with patch("builtins.input", side_effect=["1", "video_url", "n"]):
    #         main()
    #         mock_download_and_metadata.assert_called_with("video_url")

    # @patch("sys.exit")
    # def test_get_video_entries_no_entries(self, mock_exit):
    #     with patch("builtins.print") as mock_print:
    #         main.get_video_entries("playlist_url")
    #         mock_print.assert_called_with(
    #             "Something went wrong, no entries in playlist..."
    #         )
    #         mock_exit.assert_called_with(2)


if __name__ == "__main__":
    unittest.main()
