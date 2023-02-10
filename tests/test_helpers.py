# helpers_tests.py - testing with pytest
import pytest
from common_words import helpers

def test_read_input(monkeypatch):
    monkeypatch.setattr('sys.argv', ['common_words/helpers.py', './tests/test_data.txt'])
    read_data = helpers.read_input()
    assert read_data == 'abc\n123'

def test_read_input_file_not_found(monkeypatch):
    monkeypatch.setattr('sys.argv', ['common_words/helpers.py', './tests/file_that_doesnt_exist.txt'])
    with pytest.raises(FileNotFoundError):
        helpers.read_input()

def test_sanitize_text_string():
    s = "ABC-abc,x!?#$%^&*()+ y/npkl/r   abC"
    assert helpers.sanitize_text_string(s) == ['abcabcx', 'ynpklr', 'abc']

def test_sort_by_count():
    count_dict = {'b':3, 'd':1, 'a':5, 'c':65}
    assert helpers.sort_by_count(count_dict) == {'d':1, 'b':3, 'a':5, 'c':65}