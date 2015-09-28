import re
import string

source_text = open('sample.txt').read().split()
def histogram(source_text):
    histo = {}
    histo_new = {}
    for word in source_text:
        if word not in histo:
            new_word = re.sub(r"\W+", "", word)
            new_word = new_word.lstrip('_')
            new_word = new_word.rstrip('_')
            histo[new_word] = 1
        else:
            new_word = re.sub(r"\W+", "", word)
            new_word = new_word.lstrip('_')
            new_word = new_word.rstrip('_')
            histo[new_word] += 1
    for key, value in histo.items():
        histo_new[key] = (value / len(source_text))
    return histo_new


if __name__ == '__main__':
    print(histogram(source_text))
    print(len(source_text))
