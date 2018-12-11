import os
from nltk.corpus.reader.plaintext import PlaintextCorpusReader
corpusdir = '..papers/txt'
ACL_corpus = PlaintextCorpusReader(corpusdir, '.*')