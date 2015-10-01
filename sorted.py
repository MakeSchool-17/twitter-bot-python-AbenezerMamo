import random
import re
import node
import linkedlists

source_text = open('book.txt').read().split()

def histogram(source_text):
    histo = Node()
    histo.data = source_text


def format_word(word):
    re.sub(r'-_W+', '', word)
    word = word.lstrip('_-?.,"')
    word = word.rstrip('_-?.,"')
    return word

def frequency():
    pass

if __name__ == '__main__':
    """Implementation of the histogram script using the linked list data structure"""
