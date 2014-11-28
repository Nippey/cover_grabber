#!/usr/bin/env python
# Copyright (C) 2011 Jayson Vaughn <vaughn.jayson@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from setuptools import setup
import cover_grabber
import sys

extra = {}
install_requires = {}

if sys.version_info >= (3,):
    extra['use_2to3'] = True
    #extra['convert_2to3_doctests'] = ['src/your/module/README.txt']
    extra['install_requires'] = ['mutagenx']   #mutagen is not yet ported to Py3k. Progress is ongoing ("pip3.2 install mutagen" fails currently
else:
    extra['install_requires'] = ['mutagen']

setup(name='cover_grabber',
      version=cover_grabber.COVER_GRABBER_VERSION,
      description='Recursively traverse media directory and download album art',
      author='Jayson Vaughn',
      author_email='vaughn.jayson@gmail.com',
      url='https://sourceforge.net/projects/covergrabber/',
      #scripts = ['bin/covergrabber'],
      packages = ['cover_grabber','cover_grabber.downloader', 'cover_grabber.handler', 'cover_grabber.os', 'cover_grabber.logging', 'cover_grabber.bin'],
      package_dir = {'Cover Grabber':'cover_grabber'},
      entry_points={
          'console_scripts': [
              'covergrabber = cover_grabber.bin.covergrabber:main',
          ]
      },
      #install_requires = ['mutagenx'],
      license = "GNU GPL v3",
      **extra
)
