import random
import re
from linkedlists import *

source_text = open('sample.txt').read().split()

def histogram(source_text):
    histo = LinkedList()
    for word in source_text:
        word = format_word(word)
        if histo.find(word) == None:
            histo.insert([word, 1])
        else:
            histo.find(word).data[1] += 1
    return histo.head.data


def format_word(word):
    re.sub(r'-_W+', '', word)
    word = word.lstrip('_-?.,"')
    word = word.rstrip('_-?.,"')
    return word

def frequency(word):
    return histo.find(word)[1]

if __name__ == '__main__':
    """Implementation of the histogram script using the linked list data structure"""
    print(histogram(source_text))
