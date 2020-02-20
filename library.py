
import operator

class Library(object):
    def __init__(self, idx, nBook, nSign, nScan, books):
        self.id = idx
        self.nBook = nBook
        self.nSign = nSign
        self.nScan = nScan
        self.books = list(reversed(sorted(books, key=operator.attrgetter('score')) ))
        self.registered = False
        self.registeredDay = None

    def predMaxScore(self, nDays):
        restDays  = nDays - self.nSign
        if restDays < 0:
            return 0
        sumScore = 0 
        bookCap = restDays*self.nScan
        readBooks= self.books[:bookCap]
        for book in readBooks:
            sumScore += book.score
        return sumScore

    def getSol(self, nDays):
        restDays  = nDays - self.nSign
        if restDays < 0:
            return 0
        bookCap = restDays*self.nScan
        readBooksId=[book.id for book in self.books[:bookCap]]
        return readBooksId

    def __repr__(self):
        return "Lib[{}:{}:{}--{}]".format(self.nBook, self.nSign, self.nScan, self.books)


class Book(object):
    def __init__(self, id, score, scanned=False):
        self.id = id
        self.score = score

    def __repr__(self):
        return "Book[{}:{}]".format(self.id, self.score)