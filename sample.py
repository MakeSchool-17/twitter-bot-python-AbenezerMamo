import re
from sys import argv
#import pdb
import operator



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
        histo_new[key] = ((value / len(histo)))
    return histo_new

def filter_text(word):
        word = re.sub(r"\W+", "", word)
        word = word.lstrip('_')
        word = word.rstrip('_')
        return word

def compare(a):
    return a[1]

def random_sentence(word_count):
    sentence = []
    returned_histo = histogram(source_text)
    returned_histo = sorted(returned_histo.items(), reverse=True, key=compare)
    for word, freq in returned_histo[:word_count]:
        sentence.append(word)

    return sentence


if __name__ == '__main__':
    word_count = int(argv[1])
    print(*random_sentence(word_count))
