#! /usr/bin/env python3

import os
from nltk.corpus.reader.plaintext import PlaintextCorpusReader
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.collocations import FreqDist
from nltk import bigrams


class Corpus(object):

    def __init__(self, data_root):
        self.data_root = data_root
        self.data = PlaintextCorpusReader(data_root, '.*')
        self.words = self.data.words()
        self.stop = set(stopwords.words('english'))

    def documents(self):
        """Return a list of all documents in the corpus"""
        return sorted([i for i in os.listdir(self.data_root)])

    def longest_words(self):
        """Return an alphabetized list of the longest word(s)"""
        sorted_words = sorted(self.words, key=len, reverse=True)
        longest_words = [w.lower() for w in sorted_words
                         if len(w) == len(sorted_words[0])]
        return sorted(set(longest_words))

    def words_in_file(self, filename):
        """Given a file, return a list of tokenized words"""
        try:
            text = self.data.open(filename).read()
        except FileNotFoundError:
            print("The file does not exist.")
        return word_tokenize(text)

    def sentences_in_file(self, filename):
        """Given a file, return a list of sentences"""
        try:
            text = self.data.open(filename).read()
        except FileNotFoundError:
            print("The file does not exist.")
        return sent_tokenize(text)

    def tokenized_sentences_in_file(self, filename):
        """Given a file, return a list of sentences
         in which each sentence is a list of tokens"""
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
        content_words = [w.lower() for w in self.words
                         if w.lower() not in self.stop and w.isalpha()]
        content_words_dict = FreqDist(content_words)
        return content_words_dict.most_common(n_words)

    def most_frequent_bigrams(self, n_bigrams):
        """Return a list with the most frequent bigrams of content words
        in the form of pairs where the first element is the bigram and
        the second is its frequency"""
        bigram_dict = FreqDist([k for k in bigrams(self.words)if k[0].isalpha()
                       and k[1].isalpha() and len(k[0])>1 and len(k[1])>1 \
                       and k[0] not in self.stop and k[1] not in self.stop])
        return bigram_dict.most_common(n_bigrams)


if __name__ == '__main__':

    corpusdir = '../file/path'
    ACL_corpus = Corpus(corpusdir)

    print("The 100 most frequent words:")
    print(ACL_corpus.most_frequent_content_words(100))
    print()
    print("The 100 most frequent two-word phrases: ")
    print(ACL_corpus.most_frequent_bigrams(100))
