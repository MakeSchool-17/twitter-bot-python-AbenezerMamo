import re
import string

source_text = open('book.txt').read() #.split()

histo = []

#new_text = re.sub(r'[^\w]', ' ', source_text)
source_text_filtered = re.sub(r'\W+', ' ', source_text)
def histogram(source_text_filtered):
    found_at = None
    for word in source_text_filtered:
        for index, (histo_word, freq) in enumerate(histo):
            if word == histo_word:
                found = True
                found_at = index
        if not found:  # first occurence
            histo.append((word, 1))
        else:  # repeat occurence
            histo[found_at][1] += 1

def unique_words(histogram):
    return len(histo)

def frequency(word, histogram):
    return histo[word]

histogram(source_text_filtered)
print(histo)
