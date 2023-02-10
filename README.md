# common-word-sequence
This is a python application that can be run from the command line which reads text documents to find the most common sequences of words and return their counts (default 3-word sequence).

## Prerequisites
You will need to have python 3.11 installed.

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

## Known Issues, Improvements, and Thoughts
While writing functional tests, I ran into import issues with modules being called by ```pytest```. I decided to abandon these after spending some time troubleshooting the issue without success. I did stub out functional tests in ```test_common_word_sequencer.py``` showing how I might go about implementing them. The test cases are prefixed with a "x_" to avoid pytest picking them up.

Some improvements I would make given more time:
- Allow optional arguments to choose the number of words in a sequence as well as the top "n" most common sequences.
- Package the application more thoroughly to be able to distribute via Pypi to allow a one-step installation
- create a Dockerfile to allow users to build a docker image to run in a docker container for better isolation/distribution

This project included many "firsts" for me, including building a python package using best practices and using pytest for unit testing. I am also still fairly new to using Python, which meant I spent more time than usual researching solutions and reading docs. However, this was a great learning experience for me and I came away with a much better understanding of building Python applications. I spent the majority of my time on environment/boilerplate related tasks and issues, but am confident that for future projects I would be able to run through these steps much more smoothly.

One realization I had building this application was that I could use more practice in building out more thorough test suites. Aside from the testing issues mentioned above, I should have prioritized more time on creating more tests including edge case tests.

