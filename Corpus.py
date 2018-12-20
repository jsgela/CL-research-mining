#! /usr/bin/env python3

import os
from nltk.text import Text
from nltk.corpus.reader.plaintext import PlaintextCorpusReader
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.collocations import FreqDist
from nltk import bigrams, trigrams
import json

class Corpus(object):

    def __init__(self, data_root):
        self.data_root = data_root
        self.data = PlaintextCorpusReader(data_root, '.*')
        self.words = [i.lower() for i in self.data.words() if i.isalpha()]
        self.text = Text(self.words)
        self.stop = set(stopwords.words('english')).union(
            {'cid','et','al','also','and','editingboston','arxiv', 'pages',
             'trackboston','preprint','page','vol', 'volume','march','boston',
             'table'})
        with open('bib.json') as fi:
            self.bib = json.load(fi)


    def documents(self):
        """Return a list of all documents in the corpus"""
        return sorted([i for i in os.listdir(self.data_root)])

    def tokenized_sentences_in_file(self, filename):
        """Given a file name, return a list of word tokenized sentences"""
        try:
            text = self.data.open(filename).read()
            sent = []
            for s in sent_tokenize(text):
                sent.append(word_tokenize(s))
        except FileNotFoundError:
            print("The file does not exist.")
        return sent
    
    def most_frequent_content_words(self, n_words):
        """Return a list with the most frequent content words and their
        frequencies in (word, frequency) pairs ordered by frequency"""
        content_words = [w for w in self.words
            if w not in self.stop and w.isalpha() and len(w)>1]
        content_words_dict = FreqDist(content_words)
        return content_words_dict.most_common(n_words)

    def most_frequent_bigrams(self, n_bigrams):
        bigram_dict = FreqDist([k for k in bigrams(self.words)if k[0].isalpha()
            and k[1].isalpha() and len(k[0])>1 and len(k[1])>1 \
            and k[0] not in self.stop and k[1] not in self.stop])
        return bigram_dict.most_common(n_bigrams)

    def most_frequent_trigrams(self, n_trigrams):
        trigram_dict = FreqDist([k for k in trigrams(self.words)if k[0].isalpha()
            and k[1].isalpha() and len(k[0])>1 and len(k[1])>1 \
            and k[0] not in self.stop and k[1] not in self.stop
            and k[2] not in self.stop])
        return trigram_dict.most_common(n_trigrams)

    def get_info(self, fileID):
        """Return metadata associate with a file indexed by the following fields:
        author, title, booktitle, year, publisher, pages, location, doi, url"""
        return self.bib[fileID]

    def print_reference(self, fileID):
        """Print metadata (author, title of paper, title of book, publishing year)
        associated with each file as a reference"""
        d = self.bib[fileID]
        print(
            "%s. %s. %s, %s" %
            (' '.join(d['author'].split('\n')), d['title'], d['booktitle'], d['year'])
        )

    def concordance(self, word):
        self.text.concordance(word)
