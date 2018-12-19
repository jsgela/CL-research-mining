import nltk
from nltk.corpus import words, names, stopwords
from nltk.util import ngrams
from Corpus import Corpus
import re


def get_acronyms(ACL_corpus):

    #create a full list of tokenized words from the corpus
    full_text = []
    for thing in ACL_corpus.documents():
        for lsts in ACL_corpus.tokenized_sentences_in_file(thing):
            full_text.extend(lsts)

    # print(filtered_text)

    r = re.compile(r'(^[A-Z]{2,}$)')

    acronyms = sorted(set(filter(r.match, full_text)))

    filtered_acronyms = []
    for acro in acronyms:
        if acro not in filtered_acronyms:
            filtered_acronyms.append(acro)

    get_definitions(filtered_acronyms, full_text)


def get_definitions(acronyms, text):
    stop_words = set(stopwords.words('english'))

    filtered_text = []
    for x in text:
        if x.lower() not in stop_words:
            filtered_text.append(x)


    acronym_dictionary = dict()
    # acronyms_pos = {"NN", "NNS", "NNP", "VB", "JJ", "VB", "VBD", "VBG", "VBN", "VBP"}

    for acro in acronyms:
        acronym_dictionary.fromkeys(acro, None)
        acro_length = len(acro)
        ngrams_lst = ngrams(text, acro_length)
        for gram in ngrams_lst:
            count = 0
            for x, word in enumerate(gram):
                if word.isalpha() and len(word) > 2 and word[0] == acro[x]:
                    count = count+1
            if count == acro_length:
                if acronym_dictionary.get(acro) is not None:
                    acronym_dictionary[acro].append(gram)
                else:
                    acronym_dictionary[acro] = [gram]

    print(acronym_dictionary)

    print("\a")

    return acronym_dictionary


if __name__ == '__main__':
    ACL_corpus = Corpus('test')
    get_acronyms(ACL_corpus)
