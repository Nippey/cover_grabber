# -*- coding: utf-8 -*-

import os
import shutil
from nose.tools import *
from cover_grabber.handler.mp3_handler import MP3Handler

data_path = os.path.join('tests', 'data')
tmp_dir = os.path.join(data_path, 'tmp')
mp3_path = os.path.join(data_path, 'mp3')
flac_path = os.path.join(data_path, 'flac')
ogg_path = os.path.join(data_path, 'ogg')
mp3_filename = 'silence-44-s-v1.mp3'
mp3_file = os.path.join(mp3_path, mp3_filename)

mp3_special_path = os.path.join(mp3_path, 'special_chars')
mp3_special_filename = u'silence-44-s--àö.mp3'
mp3_special_file = os.path.join(mp3_special_path, mp3_special_filename)

mp3_handler = MP3Handler(mp3_path, [mp3_filename])
mp3_special_handler = MP3Handler(mp3_special_path, [mp3_special_filename])


def test_mp3_handler_init():
    assert(mp3_handler)

def test_mp3_can_get_album_and_artist_tag():
    tags = mp3_handler.get_album_and_artist()
    assert(tags == (u'Quod Libet Test Data', u'piman'))


def test_mp3_special_handler_init():
    assert(mp3_special_handler)

def test_mp3_special_can_get_album_and_artist_tag():
    tags = mp3_special_handler.get_album_and_artist()
    assert(tags == (u'Fettes Brot lässt grüßen',u'Fettes Brot'))

