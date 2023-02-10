import re
import collections
import sys

def read_input():
    complete_text = ''
    with open(sys.argv[1], 'r') if len(sys.argv) > 1 else sys.stdin as f:
        for line in f:
            complete_text = complete_text + line
    return complete_text

def sanitize_text_string(raw_txt: "str") -> "list":
    #raw_txt = """“In that day, the Lord with his sore, and great, and strong sword, shall punish Leviathan the piercing serpent,\neven Leviathan that crooked serpent; and he shall slay the drag-on that is in the sea.” —Stowe’s Annals"""
    return re.sub(r'[^\w\s]', '', raw_txt).lower().split()

def sort_by_count(dict: "dict") -> "dict":
    return {k: v for k, v in sorted(dict.items(), key=lambda item: item[1], reverse=True)}

def count_word_sequences(words: "list", n: "int") -> "dict":
    #Given a list, returns a dictionary where the keys are tuples of n-length sequences and the values are the count of the sequence.

    #Create dictionary and set initial counts equal to 0.
    count_dict = collections.defaultdict(int)

    for i in range(len(words)-n+1):
        key = tuple(words[i:i+n])
        count_dict[key] = count_dict[key] + 1
    #print(helpers.sort_by_count(count_dict))
    return sort_by_count(count_dict)

