# -*- coding: utf-8 -*-
"""
Created on Oct 17, 2016

:authors:
 * Patilla Code <patillacode@gmail.com>
"""

import json
import logging
import subprocess
import sys
import urlparse

logging.basicConfig(stream=sys.stdout,
                    level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(message)s',
                    handlers=[logging.StreamHandler()])

DOWNLOAD_FOLDER = '/tmp/'


def run_command(command):
    logging.debug('Running command `{0}`'.format(command))
    p = subprocess.Popen(
        command,
        shell=True,
        stderr=subprocess.PIPE,
        stdout=subprocess.PIPE)
    output, err = p.communicate()

    if p.returncode != 0:
        logging.error(err)
        logging.error('Problem running command: {0}'.format(command))
        # raise

    return output


def get_list_of_videos(playlist_url):
    logging.info('Gathering all videos from playlist...')
    cmd = "youtube-dl -j --flat-playlist '{0}' > yt.txt".format(playlist_url)
    return run_command(cmd)


def download_as_audio(video_id):
    cmd = "cd {0}".format(DOWNLOAD_FOLDER)
    run_command(cmd)
    cmd = ("youtube-dl -i -x --audio-format mp3 -o '{0}%(title)s-%(id)s.%(ext)s' "
           "http://www.youtube.com/watch?v={1}").format(
        DOWNLOAD_FOLDER,
        video_id)
    return run_command(cmd)


def main():
    print "Welcome to pyyt - Select your option:\n"
    print "1 - Download an entire playlist as audio\n"
    print "2 - Download a single video as audio\n"

    option = raw_input('Write your selection: ')

    if option == '1':
        url = raw_input('Please insert the youtube playlist url: ')
        get_list_of_videos(url)
        for line in open('yt.txt'):
            video = json.loads(line)
            download_as_audio(video['id'])
            logging.info("#" * 100)
            logging.info("Audio for {} is ready at {}".format(
                video['title'].encode('utf-8'), DOWNLOAD_FOLDER))
            logging.info("#" * 100)
        logging.info("*" * 100)
        logging.info("All songs have been downloaded into {}".format(
            DOWNLOAD_FOLDER))
        logging.info("*" * 100)

    elif option == '2':
        url = raw_input('Please insert the youtube video url: ')
        url_data = urlparse.urlparse(url)
        query = urlparse.parse_qs(url_data.query)
        video_id = query["v"][0]
        download_as_audio(video_id)
        logging.info("*" * 100)
        logging.info("Song has been downloaded into {}".format(
            DOWNLOAD_FOLDER))
        logging.info("*" * 100)
    else:
        logging.error('Wrong option. Cya!')


if __name__ == '__main__':
    main()
