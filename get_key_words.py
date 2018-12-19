from Corpus import Corpus
corpusdir = './test'

ACL_corpus = Corpus(corpusdir)
mfw_list = ACL_corpus.most_frequent_content_words(100)
mfb_list = ACL_corpus.most_frequent_bigrams(1000)

w_rank_dict = {}
for i in range(len(mfw_list)):
    w_rank_dict[mfw_list[i][0]] = i
w_rank_dict.pop("et")
w_rank_dict.pop("al")

key_words_1 = []
key_words_2 = []
key_word_set_1 = set()
key_word_set_2 = set()
names = []
PP = []
for (w1, w2), f in mfb_list:
    # only check bigrams with a certain frequency
    if f < 30:
        continue
    if w1.lower() not in ACL_corpus.stop and w2.lower() not in ACL_corpus.stop:
        # 1st method to clean up the bigrams
        if (w1.lower(), w2.lower()) not in key_word_set_1 and len(w1) > 2 and len(w2) > 2:
            key_words_1.append((w1, w2))
            key_word_set_1.add((w1.lower(), w2.lower()))
        
        # 2nd method to clean up the bigrams
        r1 = w_rank_dict.get(w1.lower())
        r2 = w_rank_dict.get(w2.lower())
        if not r1 == None and not r2 == None:
            if (w1.lower(), w2.lower()) not in key_word_set_2:
                key_words_2.append((w1, w2))
                key_word_set_2.add((w1.lower(), w2.lower()))
        elif r1 == None and r2 == None and w1.istitle() and w2.istitle(): # trying to get names
            names.append((w1, w2))
        if w1.isupper() and not w2.isupper(): # trying to get proper nouns
            PP.append((w1, w2))

print("key_words_1\n", key_words_1)
print("\nkey_words_2\n", key_words_2)
print("\nnames\n", names)
print("\nPP\n", PP)
