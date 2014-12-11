import os
import sys
import shutil
import unittest
from nose.tools import *
from cover_grabber.handler.mp3_handler import MP3Handler

PY3 = sys.version_info >= (3,)

data_path = os.path.join('tests', 'data')
tmp_dir = os.path.join(data_path, 'tmp')
mp3_path = os.path.join(data_path, 'mp3')
flac_path = os.path.join(data_path, 'flac')
ogg_path = os.path.join(data_path, 'ogg')
mp3_filename = 'silence-44-s-v1.mp3'
mp3_file = os.path.join(mp3_path, mp3_filename)

mp3_handler = MP3Handler(mp3_path, [mp3_filename])


class mp3_handler_tests(unittest.TestCase):

    def ustr(self,s):
        if PY3:
            return s
        else:
            return str(s)
            
    def test_mp3_handler_init(self):
        assert(mp3_handler)

    def test_mp3_can_get_album_and_artist_tag(self):
        tags = mp3_handler.get_album_and_artist()
        assert(tags == (self.ustr('Quod Libet Test Data'), self.ustr('piman')))


