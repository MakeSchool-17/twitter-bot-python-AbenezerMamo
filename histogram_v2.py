import re
import string

source_text = open('book.txt').read() #.split()

histo = []

#new_text = re.sub(r'[^\w]', ' ', source_text)
source_text_filtered = re.sub(r'\W+', ' ', source_text)
def histogram(source_text_filtered):
    index = 0
    for word in source_text_filtered:
        if word not in histo:
            histo.append((word, 0))
            index += 1
        else:
            histo[index][1] += 1
            index += 1

def unique_words(histogram):
    return len(histo)

def frequency(word, histogram):
    return histo[word]

histogram(source_text_filtered)
print(histo)
