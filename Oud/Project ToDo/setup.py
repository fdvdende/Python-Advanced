from setuptools import setup

with open("README.md", 'r') as f:
   long_description = f.read()

setup(
   name='ToDo',
   version='1.0',
   description='A ToDo application for demonstration purposes',
   long_description=long_description,
   license="MIT",
   author='Peter Anema',
   author_email='email@peteranema.nl',
   packages=['toto'],  #same as name
   install_requires=[], #external packages as dependencies
)
