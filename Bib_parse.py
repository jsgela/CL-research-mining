import os
import bibtexparser
import json

#os.chdir('./bib/')

all_bib = {}
for filename in os.listdir('.'):
    with open(filename) as bib_file:
        bib_data = bibtexparser.load(bib_file)
    entry = bib_data.entries[0]
    all_bib[entry['ID']] = entry


with open('../bib.json', 'w') as output:
    json.dump(all_bib, output)
