import re
import string

source_text = open('sample.txt').read().split()


histo = {}
histo_new = {}
def histogram(source_text):
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
        for word in histo:
            histo_new[word] /= len(source_text)


def random_sentence():
    histogram(source_text)
    for key, value in histo_new:
        if value >= 0:
            sentence.append(key)
    return sentence



if __name__ == '__main__':
    print(random_sentence())
