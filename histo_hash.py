import hash_table

source_text = open('sample.txt').read().split()

def histogram(source_text):
    hushhh = HashTable()
    for word in source_text
        if word in hushhh.keys:
            data = hushhh.get(word)
            hushhh.update(key, data += 1)
        else:
            hushhh.set(word, 1)
    return hushhh

def frequency(word, hushhh):
    return hushhh.get(word)






if __name__ == '__main__':
    print(histogram(source_text))
