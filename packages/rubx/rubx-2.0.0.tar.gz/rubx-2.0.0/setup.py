#!/bin/python
from distutils.core import setup
setup(
  name = 'rubx',
  packages = ['rubx'],
  version = '2.0.0',
  license='MIT', 
  description = '[*] > a module or library for rubika messenger from iran !',
  long_description='```info for library in < github.com/mester-root/rubx >```',
  author = 'Saleh',
  author_email = 'm3st3r.r00t@gmail.com',
  url = 'https://github.com/mester-root/rubx',
  download_url = 'https://github.com/mester-root/rubx',
  keywords = ["Rubika","RubiThon","rubithon","rubx","rubix","rubikax","rubika","bot","robot","library","rubikalib","rubikalibrary","rubika.ir","web.rubika.ir","m.rubika.ir"],
  install_requires=[
          'requests',
          'pycryptodome==3.10.1',
          'urllib3',
          'tqdm',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',   
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
  ],
)