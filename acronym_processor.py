import nltk
from nltk.corpus import words, names, stopwords
from nltk.util import ngrams
from Corpus import Corpus
import re
import time


def get_acronyms(ACL_corpus):
    # r = re.compile(r'(^[A-Z]{2,}$)')
    # acronyms = sorted(set(filter(r.match, full_text)))

    full_text = ACL_corpus.words

    acronyms = {elm for elm in full_text if elm.isupper() and elm.isalpha() and len(elm) > 1}
    #    print(acronyms)
    return get_definitions(list(acronyms), full_text)


def get_definitions(acronyms, text):
    stop_words = set(stopwords.words('english'))

    filtered_text = []
    for x in text:
        if x.lower() not in stop_words:
            filtered_text.append(x)

    # acronyms = acronyms[:100]
    acronym_dictionary = {}

    a = time.time()
    k = 0
    for acro in acronyms:
        if k % 20 == 0:
            print(k)
        k += 1
        acro_len = len(acro)
        matches = set()
        for i in range(len(filtered_text) - acro_len):
            chosen = True
            for j in range(acro_len):
                if len(filtered_text[i + j]) < 2 or not filtered_text[i + j][0] == acro[j] or filtered_text[
                    i + j].isupper():
                    chosen = False
                    break
            if chosen:
                word = ' '.join(filtered_text[i:i + acro_len])
                matches.add(word)
        if not len(matches) == 0:
            acronym_dictionary[acro] = list(set(matches))

    b = time.time()
    #    print(len(acronym_dictionary))
    #    print(acronym_dictionary)
    print("Time", b - a)

    return acronym_dictionary


if __name__ == '__main__':
    ACL_corpus = Corpus('test')
    acro_dict = get_acronyms(ACL_corpus)
    with open("acro_dict.txt", "w", encoding="utf-8") as out_file:
        for key in acro_dict.keys():
            out_file.write(key)
            for w in acro_dict[key]:
                out_file.write("," + w)
            out_file.write("\n")
