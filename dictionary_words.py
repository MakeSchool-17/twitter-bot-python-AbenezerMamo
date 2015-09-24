import random
from sys import argv

content = open('/usr/share/dict/words').read().split()

words_list = []
for words in content:
    words_list.append(words)

sentence = []
while len(sentence) < int(argv[1]):
    sentence.append(words_list[random.randint(0, len(words_list))])

print(*sentence)
