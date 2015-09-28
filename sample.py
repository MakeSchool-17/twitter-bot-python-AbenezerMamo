import re
import string
import random
from sys import argv
import pdb



source_text = open('sample.txt').read().split()
def histogram(source_text):
    histo = {}
    histo_new = {}
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

def random_sentence(word_count):
    sentence = []
    returned_hist = histogram(source_text)
    #histo_new = sorted(histo_new.items(), key=operator.itemgetter(1))
    counter = 0
    while counter < word_count:
        for word, freq in returned_hist.items():
            if freq >= .02: #(1 - (word_count / len(histo_new))):
                sentence.append(word)
        counter += 1

    return sentence


if __name__ == '__main__':
    word_count = int(argv[1])
    print(random_sentence(word_count))
