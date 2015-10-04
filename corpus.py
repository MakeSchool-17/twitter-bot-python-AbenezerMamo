import wget

file_url = "http://www.gutenberg.org/cache/epub/3253/pg3253.txt"
file_name = wget.download(file_url, out='corpus_dl.txt')
