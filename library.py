
import operator

class Library(object):
    def __init__(self, idx, nBook, nSign, nScan, books):
        self.id = idx
        self.nBook = nBook
        self.nSign = nSign
        self.nScan = nScan
        self.books = list(reversed(sorted(books, key=operator.attrgetter('score')) ))
        self.tempBooks = self.books[:]
        self.registered = False
        self.registeredDay = None
        self.solBooks = []

    def predMaxScore(self, nDays, readBookSet):
        restDays  = nDays - self.nSign
        if restDays < 0:
            return 0, []
        unReadBooks = set([book.id for book in self.tempBooks]) - readBookSet
        newBooks = []
        for book in self.tempBooks:
            if book.id in unReadBooks:
                newBooks.append(book)
        self.tempBooks = newBooks
        sumScore = 0 
        bookCap = restDays*self.nScan
        readBooks= self.tempBooks[:bookCap]
        readBooksId=[book.id for book in self.tempBooks[:bookCap]]
        for book in readBooks:
            sumScore += book.score
        return sumScore, readBooksId

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