#!/usr/bin/env python3
import os
from distutils.core import setup

version = {}
with open(os.path.join(os.path.dirname(__file__), 'tech_console', 'version.py'), 'r') as vf:
    exec(vf.read(), version)

setup(name='tech_console',
      version=version['__version__'],
      packages=['tech_console'],
      description='Technician console for Helios project LARP',
      author='Yuval Moran',
      author_email='yuvalg@gmail.com',
      url='https://github.com/gmyuval/tech-console',
      install_requires=[
          'bitarray>=0.8.3',
          'prompt-toolkit>=2.0.7',
          'bcrypt>=3.1.4',
      ],
      entry_points={
          'console_scripts': [
              'techconsole=main:main'
          ]
      }
      )
