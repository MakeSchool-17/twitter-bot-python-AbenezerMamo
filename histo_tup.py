import random
import re
from sys import argv
import time

source_text = open('book.txt').read().split()

#method 1

def histogram(source_text):
    histo = []
    index = 0
    for word in source_text:
        filter(word)
        if word in histo:
            histo.append((word, 0))
            index += 1
        else:
            histo[index][1] += 1
            index += 1

    return histo


def filter(word):
    re.sub(r'-_W+', '', word)
    word = word.lstrip('_-?.,"')
    word = word.rstrip('_-?.,"')
    return word



if __name__ == '__main__':
    print(histogram(source_text))
