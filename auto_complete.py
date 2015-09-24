from sys import argv


content = open('/usr/share/dict/words').read().split()
uncompleted_word = argv[1]
uncompleted_word_len = len(uncompleted_word)

search_keys = uncompleted_word

possible_words = []


for word in content:
    index = 1
    while word[:index] == search_keys[:index]:
        index += 1
        if index > uncompleted_word_len:
            possible_words.append(word)
print(possible_words)


#You would use the code below if you wanted to solve this using recursion
#Thank you Jared for your assistance with this!
"""
def matches(word, search_keys, index=1):
    if index == len(search_keys):
        return True
    if word[:index] == search_keys[:index]:
        return matches(word, search_keys, index + 1)
    else:
        return False
"""
