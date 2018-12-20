from nltk.collocations import FreqDist
from wordcloud import WordCloud
import re

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
    email_regex = re.compile(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+")
    emails = []
    for file in corpus.documents():
        text = corpus.sentences_in_file(file)[0]
        emails.extend(re.findall(email_regex, text))
    return emails


def get_meaningful_bigrams(corpus, mfw_list, mfb_list):
    w_rank_dict = {}
    for i in range(len(mfw_list)):
        w_rank_dict[mfw_list[i][0]] = i
    
    keywords = []
    keyword_set = set()
    for (w1, w2), f in mfb_list:
        # only check bigrams with a certain frequency
        if f < 30:
            continue
        if w1.lower() not in corpus.stop and w2.lower() not in corpus.stop:
            # clean up the bigrams
            r1 = w_rank_dict.get(w1.lower())
            r2 = w_rank_dict.get(w2.lower())
            if not r1 == None and not r2 == None:
                if (w1.lower(), w2.lower()) not in keyword_set:
                    keywords.append((w1, w2))
                    keyword_set.add((w1.lower(), w2.lower()))
    return keywords


def _get_acro_dict():
    with open("acro_dict.txt") as in_file:
        acro_dict = {}
        for line in in_file:
            tokens = line.strip().split(",")
            key = tokens.pop(0)
            acro_dict[key] = tokens
    return acro_dict


def get_acro_keywords(mfw_list):
    acro_dict = _get_acro_dict()
    keywords =[]
    for w in mfw_list:
        matchs = acro_dict.get(w.upper())
        if not matchs == None:
            keywords.extend(matchs)
    return keywords

