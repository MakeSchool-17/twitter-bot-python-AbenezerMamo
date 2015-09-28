import re
import string
import random
from sys import argv

word_count = len(argv)
sentence = []
histo = {}

source_text = open('sample.txt').read().split()
def histogram(source_text):
    for word in source_text:
        if word not in histo:
            filter_text(word)
            histo[word] = 1
        else:
            filter_text(word)
            histo[word] += 1
    for key, value in histo.items():
        histo_new[key] = (value / len(source_text))
    return histo_new

def filter_text(word):
        word = re.sub(r"\W+", "", word)
        word = word.lstrip('_')
        word = word.rstrip('_')
        return word

def random_sentence():
    histogram(source_text)
    #histo_new = sorted(histo_new.items(), key=operator.itemgetter(1))
    while counter < word_count:
        for key, value in histo_new:
            if value > (1 - (word_count / len(histo_new))):
                sentence.append(key)
    return sentence.items()


if __name__ == '__main__':
    print(random_sentence)
