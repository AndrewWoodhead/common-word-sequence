# common-word-sequence
This is a python application that can be run from the command line which reads text documents to find the most common sequences of words and return their counts (default 3-word sequence).

## Setup
To set up the application locally, you will want to follow these steps:
- clone the repo into a local directory:
```
git clone https://github.com/AndrewWoodhead/common-word-sequence.git
```
- run the project in a virtual environment:
```
python -m venv venv

.\venv\Scripts\activate
```
- install the necessary packages and dependencies:
```
pip install -e .
```
That's it. The project should now be running in a virtual environment and the application can now be run.

## How to run the application
To run the app, first ```cd``` into the common_words directory. 
You can either pass run the application and pass in a list of .txt files as arguments:
```
python -m common_word_sequencer \path\to\file_1.txt \path\to\file_2.txt
```
or you can use stdin:
```
# Windows example
type \path\to\files\*.txt | python -m common_word_sequence
```
Two .txt files are provided under the ```.\tests\test_files``` directory as well.

By default, the program will return the first 100 most common sequences of three words from the files provided as stdout.

## How to run tests
The package includes ```pytest``` for testing. Unit tests are under the ```/tests``` directory. To run the test runner, which runs all tests, ```cd``` into the root of your project, then simply run: ```pytest```
