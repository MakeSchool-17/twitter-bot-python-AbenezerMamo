from sys import argv
import re


content = open(argv[1]).read().split()



def filter(content):
    for word in content:
        filter(word)


def filter_word(word):
    word = re.sub(r"\W+", "", word)
    word = word.lstrip('_')
    word = word.rstrip('_')
    return word



if __name__ == '__main__':
    file_name = 'filtered_corpus.txt'
    filter(content)
