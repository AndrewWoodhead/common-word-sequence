from setuptools import setup, find_packages

with open("README.md", 'r') as f:
    long_description = f.read()

setup(
   name='common_word_sequence',
   version='1.0',
   description='A module to get the most common word sequences from text documents.',
   long_description=long_description,
   author='Andrew Woodhead',
   author_email='awoodhea@gmail.com',
   url="https://github.com/AndrewWoodhead/common-word-sequence",
   packages=find_packages(),
   install_requires=['pytest']
)