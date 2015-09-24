import random
content = open('/usr/share/dict/words').read().split()
words_list = []
for words in content:
    words_list.append(words)
sentence = []
while len(sentence) < 5:
    sentence.append(words_list[random.randint(0, len(words_list))])
print(*sentence)
