from sys import argv
import re
import logging


content = open(argv[1]).read().split()

words_list = []

def filter(content, file_name):
    for word in content:
        filter_word(word)
        words_list.append(word)

    file_name.write(words_list)


def filter_word(word):
    word = re.sub(r"\W+", "", word)
    word = word.lstrip('_')
    word = word.rstrip('_')
    return word



if __name__ == '__main__':
    file_name = 'filtered_corpus.txt'
    filter(content, file_name)
    logging.info('Content has been filtered and sent to the filtere content file')
