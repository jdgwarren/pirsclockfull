#! /usr/bin/env python

from distutils.core import setup
from setuptools import setup
setup(name='PiRSClock-Full',
      version='2.0',
      description='Raspberry Pi Radio Studio Clock with Studio Indicators',
      author='Peter Symonds',
      author_email='peter@engineeringradio.co.uk',
      url='http://github.com/Engineeringradio/pirsclockfull',
      scripts=['pirsclockfull'],
      requires=['pygame','RPi.GPIO'],
      install_requires=['pygame','RPi.GPIO'],
      classifiers=[
          'Development Status :: 4 - Beta',
          'Environment :: Console',
          'Environment :: Console :: Framebuffer',
          'Intended Audience :: System Administrators',
          'Intended Audience :: Customer Service',
          'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Operating System :: POSIX :: Linux',
          'Topic :: Utilities',
          ],
      )
