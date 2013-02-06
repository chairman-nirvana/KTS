# -*- coding:utf-8 -*-
import sys
sys.path.append('./src')
from distutils.core import setup
from kts import __version__

setup(name='kts',
      version=__version__,
      description='Kill Time Secretary',
      long_description=open("README.md").read(),
      author='chairman',
      author_email='chairman.nirvana@dont.contact.me',
      packages=['kts'],
      package_dir={'kts': 'src/kts'},
      package_data={'kts': ['stuff']},
      license="Public domain",
      platforms=["any"],
      url='https://github.com/chairman-nirvana/KTS.git')
