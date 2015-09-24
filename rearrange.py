from sys import argv
import getopt
import random

words = []
for args in argv:
    words.append(args)
words.remove(argv[0])

random.shuffle(words)
for word in words:
    print(word)
