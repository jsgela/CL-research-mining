from Corpus import Corpus
from wordcloud import WordCloud
from nltk.collocations import FreqDist
import re

corpusdir = './paper'

ACL_corpus = Corpus(corpusdir)

email_regex = re.compile(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+")

def word_cloud(word_list):
    total = sum(i[1] for i in word_list)
    freq = {i[0]:(i[1]/total) for i in word_list}
    # Generate a word cloud image
    wc = WordCloud(max_font_size=40, min_font_size=8, width=600, height=400)
    wc.generate_from_frequencies(freq)
    # Display the generated image
    image = wc.to_image()
    image.show()


def geo_distribution(corpus):
    locations = []
    for file in corpus.documents():
        info = corpus.get_info(file[:-4])
        if 'location' in info:
            locations.append(info['location'])
    fd = FreqDist(locations)
    fd.pprint()
    fd.plot()


def extract_email(corpus):
    for file in corpus.documents():
        text = corpus.sentences_in_file(file)[0]
        emails = re.findall(email_regex, text)
    return emails


# Tests
# print(ACL_corpus.get_info('W18-4106')['author'])
# ACL_corpus.concordance('language')

# Generator frequent topic lists from the corpus
# single_word_list = ACL_corpus.most_frequent_content_words(100)
bigram_list = ACL_corpus.most_frequent_bigrams(100)
trigram_list = ACL_corpus.most_frequent_trigrams(100)
# print("Top 100 most frequent words:")
# print(single_word_list)
# print()
# print("Top 100 most frequent phrases: ")
# print(set(bigram_list),set(trigram_list))

# Create word cloud images
# print("Generating word cloud for most frequent words...")
# word_cloud(single_word_list)
# print("Generating word cloud for most frequent bigrams...")
# word_cloud([(' '.join(i),j) for i,j in bigram_list])
# print("Generating word cloud for most frequent trigrams...")
# word_cloud([(' '.join(i),j) for i,j in trigram_list])

# Count number of papers by location
# print("Number of papers by location: ")
# geo_distribution(ACL_corpus)

