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
            raise

        return output


def get_list_of_videos(playlist_url):
    cmd = "youtube-dl -j --flat-playlist '{0}' > yt.txt".format(playlist_url)
    return run_command(cmd)


def download_as_audio(video):
    logging.info('Downloading and converting to audio {0}'.format(
        video['title']))
    cmd = "cd {0}".format(DOWNLOAD_FOLDER)
    run_command(cmd)
    cmd = ("youtube-dl -x --audio-format mp3 -o '{0}%(title)s-%(id)s.%(ext)s' "
           "http://www.youtube.com/watch?v={1}").format(
        DOWNLOAD_FOLDER,
        video['id'])
    return run_command(cmd)


def main():
    print "Welcome to pyyt - Select your option:\n"
    print "1 - Download an entire playlist as audio\n"

    option = raw_input('Write your selection: ')

    if option == '1':
        url = raw_input('Please insert the youtube playlist url: ')
        get_list_of_videos(url)
        for line in open('yt.txt'):
            video = json.loads(line)
            download_as_audio(video)
            logging.info("#" * 100)
            logging.info("Audio for {} is ready at {}".format(
                video['title'], DOWNLOAD_FOLDER))
            logging.info("#" * 100)
        logging.info("*" * 100)
        logging.info("All songs have been downloaded in {}".format(
            DOWNLOAD_FOLDER))
        logging.info("*" * 100)

    else:
        logging.error('Wrong option. Cya!')


if __name__ == '__main__':
    main()
