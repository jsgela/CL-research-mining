from Corpus import Corpus
from TaggedInstance import TaggedInstance


class TaggedCorpus(Corpus):
    
    def __init__(self, data_root):
        Corpus.__init__(self, data_root)
    
    def instances(self):
        insts = []
        for id in self.documents()[:4]:
            tags = []
            authors = []
            sents = self.tokenized_sentences_in_file(id)
            inst = TaggedInstance(id, tags, authors, sents)
            insts.append(inst)

        return insts


if __name__ == "__main__":
    corpusdir = './test'
    a = TaggedCorpus(corpusdir)
    print(*a.instances())
    
