import os
import shutil
import unittest
from nose.tools import *
from cover_grabber.handler.ogg_handler import OGGHandler

data_path = os.path.join('tests', 'data')
tmp_dir = os.path.join(data_path, 'tmp')
mp3_path = os.path.join(data_path, 'mp3')
flac_path = os.path.join(data_path, 'flac')
ogg_path = os.path.join(data_path, 'ogg')
ogg_filename = 'stallmanupv.ogg'
ogg_file = os.path.join(ogg_path, ogg_filename)

ogg_handler = OGGHandler(ogg_path, [ogg_filename])


class ogg_handler_tests(unittest.TestCase):

    def test_ogg_handler_init(self):
        assert(ogg_handler)

    def test_ogg_can_get_album_and_artist_tag(self):
        tags = ogg_handler.get_album_and_artist()
        assert(tags)


