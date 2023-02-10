from common_words import helpers

def test_count_word_sequences():
    word_list = ['this','is','a','test','this','is','a','different','test','that','is','a','test']
    expected_result = { ('this', 'is', 'a'): 2, ('is', 'a', 'test'): 2, ('a', 'test', 'this'): 1, 
                        ('test', 'this', 'is'): 1, ('is', 'a', 'different'): 1, ('a', 'different', 'test'): 1, 
                        ('different', 'test', 'that'): 1, ('test', 'that', 'is'): 1, ('that', 'is', 'a'): 1
                        }
    assert helpers.count_word_sequences(word_list, 3) == expected_result