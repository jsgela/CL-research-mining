from nltk import sent_tokenize, word_tokenize
import Corpus
from Corpus import Corpus
import re
from nltk.corpus import words, names

def get_acronyms(ACL_corpus):

    full_text = []

    for thing in ACL_corpus.documents():
        for lsts in ACL_corpus.tokenized_sentences_in_file(thing):
            full_text.extend(lsts)

    r = re.compile(r'(^[A-Z]{2,}$)')

    acronyms = set(filter(r.match, full_text))

    print(acronyms)

    # filtered_acros = [acro for acro in acronyms if acro.lower not in words.words()]
    # for acro in acronyms:
    #     if acro.lower() not in set(words.words()) and acro not in set(names.words()):
    #         filtered_acros.append(acro)

    # print(filtered_acros)




if __name__ == '__main__':
    ACL_corpus = Corpus('text data')
    get_acronyms(ACL_corpus)