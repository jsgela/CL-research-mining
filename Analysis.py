from Corpus import Corpus
from analysis_util import * 

corpusdir = './paper'
ACL_corpus = Corpus(corpusdir)
single_word_list = ACL_corpus.most_frequent_content_words(100)
bigram_list = ACL_corpus.most_frequent_bigrams(100)
trigram_list = ACL_corpus.most_frequent_trigrams(100)


# Generator frequent topic lists from the corpus
print("Top 100 most frequent words:")
print(single_word_list)
print()
print("Top 200 most frequent phrases: ")
print(set(bigram_list),set(trigram_list))

# Create word cloud images
print("Generating word cloud for most frequent words...")
word_cloud(single_word_list)
print("Generating word cloud for most frequent bigrams...")
word_cloud([(' '.join(i),j) for i,j in bigram_list])
print("Generating word cloud for most frequent trigrams...")
word_cloud([(' '.join(i),j) for i,j in trigram_list])

        
# Generate possible trending bigrams by comparing frequent words and frequent bigrams
print("Possible trending bigrams: ")
print(get_meaningful_bigrams(ACL_corpus, single_word_list, bigram_list))


# Generate possible trending words using the acronym dictionary
l = []
for (w1, w2), f in bigram_list:
    l.append(w1)
    l.append(w2)
print("Possible trending words using the acronym dictionary: ")
print(get_acro_keywords(l))


# Count number of papers by location
print("Number of papers by location: ")
geo_distribution(ACL_corpus)
