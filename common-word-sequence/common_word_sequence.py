
import string
import re
import collections

def main():
    s = """“In that day, the Lord with his sore, and great, and strong sword, shall punish Leviathan the piercing serpent, 
    even Leviathan that crooked serpent; and he shall slay the dragon that is in the sea.” —Stowe’s Annals"""
    #s = s.translate(str.maketrans('', '', string.punctuation)).lower()
    words = re.sub(r'[^\w\s]', '', s).lower().split()
    print(words)
    countSequences(words, 3)

def countSequences(words,n):
    #Given a list, returns a dictionary mapping each n-element sequence tuple to its number of occurrences in the list.

    # Initialize all counts implicitly to 0.
    countDict = collections.defaultdict(int)

    for i in range(len(words)-n+1):
        key = tuple(words[i:i+n])
        countDict[key] = countDict[key] + 1
    #print(countDict)
    return countDict

    
if __name__ == '__main__':
    main()