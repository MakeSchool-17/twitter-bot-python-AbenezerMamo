import random
import re
import linkedlists

source_text = open('book.txt').read().split()

def histogram(source_text):
    histo = LinkedList()
    for word in source_text:
        if histo.find(word) == None:
            histo.insert(word, 0)
        else:
            pass


def format_word(word):
    re.sub(r'-_W+', '', word)
    word = word.lstrip('_-?.,"')
    word = word.rstrip('_-?.,"')
    return word

def frequency(word):
    histo.find(word)

if __name__ == '__main__':
    """Implementation of the histogram script using the linked list data structure"""
