from cStringIO import StringIO
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
import os
import sys, getopt
import nltk.tokenize
import nltk
from pathlib import Path
import codecs

#converts pdf, returns its text content as a string
def convert(fname, pages=None):
    if not pages:
        pagenums = set()
    else:
        pagenums = set(pages)

    output = StringIO()
    manager = PDFResourceManager()
    converter = TextConverter(manager, output, laparams=LAParams())
    interpreter = PDFPageInterpreter(manager, converter)

    infile = file(fname, 'rb')
    for page in PDFPage.get_pages(infile, pagenums):
        interpreter.process_page(page)
    infile.close()
    converter.close()
    text = output.getvalue()
    output.close
    return text 
   
def convertMultiple(pdfDir, txtDir):
    if pdfDir == "": pdfDir = os.getcwd() + "\\" #if no pdfDir passed in 
    for pdf in os.listdir(pdfDir): #iterate through pdfs in pdf directory
        fileExtension = pdf.split(".")[-1]
        if fileExtension == "pdf":
            pdfFilename = pdfDir + pdf 
            text = convert(pdfFilename) #get string of text content of pdf
            textFilename = txtDir + pdf + ".txt"
            textFile = open(textFilename, "w") #make text file
            textFile.write(text) #write text to text file
            #textFile.close

pdfDir = "C:/Users/86136/Desktop/HW/IntroNLP/Final Project/con27/pdf/"
txtDir = "C:/Users/86136/Desktop/HW/IntroNLP/Final Project/Data/Papers_txt/"
convertMultiple(pdfDir, txtDir)

# pick out those without space
def pickout(path):
     file_lst = [f.name for f in Path(path).iterdir() if f.is_file()]
     for filename in file_lst:
        full_path = path+filename
        with codecs.open(full_path, 'r', encoding="utf-8") as f:
            r = f.read()
            w_lst= nltk.word_tokenize(r)
            for w in w_lst:
                if len(w) >= 100:
                    f.close()
                    os.remove(full_path)
                    break
pickout(txtDir)