import PyPDF4, re

class Indexer:

    def __init__(self, file):
        self.file = file
        self.__index = {}
        self.__stop_words = open("stopwords/stopwords.txt", "r").read()

    def extractWords(self, text):
        words = []
        for word in re.split('\n| ', text):
            if word.isalnum():
                if(word not in self.__stop_words):
                    words.append(word.lower())
        return words

    def addToIndex(self, words, page):
        for word in words:
            if word in self.__index:
                self.__index[word].append(page)
            else:
                self.__index[word] = [page]

    def getPdfWords(self, file):
        pdfFileObj = open(file, 'rb')
        pdfReader = PyPDF4.PdfFileReader(pdfFileObj)
        i = 0
        while i < pdfReader.numPages:
            pageObj = pdfReader.getPage(i)
            words = self.extractWords(pageObj.extractText())
            self.addToIndex(words, i)
            i += 1

    def createReverseIndex(self):
        self.getPdfWords(self.file)
        return self.__index

Economics = Indexer("Economics-2018.pdf")
index = Economics.createReverseIndex()
