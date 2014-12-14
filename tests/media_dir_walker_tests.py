# -*- coding: utf-8 -*-

import os
import shutil
from nose.tools import *
from cover_grabber.os.media_dir_walker import MediaDirWalker

data_path = os.path.join('tests', 'data')
tmp_path = os.path.join(data_path, 'tmp')
tmp_special_path = os.path.join(data_path, 'tmp_special')
mp3_path = os.path.join(data_path, 'mp3')
flac_path = os.path.join(data_path, 'flac')
ogg_path = os.path.join(data_path, 'ogg')

walker = MediaDirWalker(data_path)


def setup():
    remove_dir_if_exists(tmp_path)
    remove_dir_if_exists(tmp_special_path)

    os.mkdir(tmp_path)
    os.mkdir(tmp_special_path)
    
def remove_dir_if_exists(path):
    if os.path.exists(path):
        empty_dir(path)
        os.rmdir(path)
        
def empty_dir(path):
    for file_name in os.listdir(path):
        os.remove(os.path.join(path, file_name))

def teardown():
    empty_dir(tmp_path)
    os.rmdir(tmp_path)
    empty_dir(tmp_special_path)
    os.rmdir(tmp_special_path)


def test_media_dir_walker_init():
    assert(walker)

def test_media_dir_walker_path():
    assert(walker.path == data_path)

def test_cover_doesnt_exist():
    assert(walker.check_cover_image_existence(mp3_path) == False)

def test_cover_exists():
    assert(walker.check_cover_image_existence(ogg_path) == True)

def test_can_get_image_url():
    assert(("http://" in walker.get_image_url('Abbey Road', 'The Beatles')) == True)

def test_can_download_image():
    image_url = walker.get_image_url('Abbey Road', 'The Beatles')
    walker.download_image(tmp_path, image_url)
    assert(("cover" in os.listdir(tmp_path)[0].split('.')[0]) == True)
    
    
def test_can_get_special_image_url():
    assert(("http://" in walker.get_image_url(u'Fettes Brot lässt grüßen', u'Fettes Brot')) == True)
    
def test_can_download_special_image():
    image_url = walker.get_image_url(u'Fettes Brot lässt grüßen', u'Fettes Brot')
    walker.download_image(tmp_special_path, image_url)
    assert(("cover" in os.listdir(tmp_special_path)[0].split('.')[0]) == True)
    
    
