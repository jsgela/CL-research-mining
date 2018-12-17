from . import Corpus
corpusdir = './test'

ACL_corpus = Corpus(corpusdir)

print("The 100 most frequent content words:")
print(ACL_corpus.most_frequent_content_words(100))
print()
print("The 100 most frequent bigrams containing only content words: ")
print(ACL_corpus.most_frequent_bigrams(100))