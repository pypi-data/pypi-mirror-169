from setuptools import setup, find_packages

setup (
  name='robotstxtinterpreter',
  version='1.0',
  license='MIT',
  author='randomsoftwareshack',
  author_email='lolimnotputtingmyactualemail@poopmap.net',
  packages=find_packages('src'),
  package_dir = {'': 'robotstxtinterpreter'},
  url = 'https://github.com/randomsoftwareshack/robotstxtinterpreter/',
  keywords='robots.txt',
  install_requires=[
    'requests',
  ], 
)
