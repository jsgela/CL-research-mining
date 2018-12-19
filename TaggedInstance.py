class TaggedInstance(object):
    
    def __init__(self, fileid, tags, authors, sents):
        self.fileid = fileid
        self.tags = tags
        self.authors = authors
#        self.all_sents = [["This", "is", "a", "test"], ["Second", "sent"]]   # tokenized_sents
        self.all_sents = sents 

    def words(self):
        words = []
        for sent in self.all_sents:
            words.extend(sent)
        return words

    def sents(self):
        return self.all_sents

    def __str__(self):
        return "TaggedInstance(fileid='" + self.fileid + "', tags=" + self.tags.__str__()                            + ", authors=" + self.authors.__str__() + ")"
