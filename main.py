
from library import Library, Book
import numpy as np

class Problem(object):
    def __init__(self, filename):
        print('file--', filename)
        f = open(filename)
        l = f.readline().split(' ')
        self.filename = filename
        self.nBooks, self.nLibs, self.nDays = int(l[0]), int(l[1]), int(l[2])
        self.books = [ Book(i,int(score)) for i, score in enumerate(f.readline().split(' '))]
        sumb = 0
        for b in self.books:
            sumb += b.score
        print( sumb/1000000 )
        self.book2Score = {book.id: int(book.score) for book in self.books}
        self.libs = []
        for libId in range(self.nLibs):
            l = [int(i) for i in f.readline().split(' ')]
            nBooks, nSign, nScan = l[0], l[1], l[2]
            books = [ Book(int(i), int(self.book2Score[int(i)])) for i in f.readline().split(' ') ] 
            lib = Library(libId, nBooks, nSign, nScan, books)
            self.libs.append(lib) 
        self.pri()

    def solve(self):
        t = 0
        solution = []
        readBookSet  = set()
        while t < self.nDays:
            print('-----', t)
            scoreList = []
            readBookList = []
            for lib in self.libs:
                if lib.registered == False:
                    score, curBookList = lib.predMaxScore(self.nDays - t, readBookSet)
                    scoreList.append( score )
                    readBookList.append( curBookList )
                else:
                    scoreList.append(0)
                    readBookList.append( [ ] )
            if len(scoreList) == 0:
                break
            if max(scoreList) == 0:
                break
            libIndex = scoreList.index(max(scoreList))
            self.libs[libIndex].registeredDay = t
            self.libs[libIndex].registered = True
            self.libs[libIndex].solBooks = readBookList[libIndex]
            readBookSet = readBookSet.union(readBookList[libIndex])
            solution.append(self.libs[libIndex])
            t += self.libs[libIndex].nSign
        print([(lib.id, lib.nSign, lib.registeredDay) for lib in solution])
        return solution

    def dump(self, solution):
        f = open(self.filename.replace('data/', 'out/'), 'w+')
        f.write('{}\n'.format(len(solution)))
        for lib in solution:
            books = lib.solBooks
            f.write('{} {}\n'.format(
                lib.id, len(books)
            ))
            s = ""
            for book in books:
                s+= str(book) + ' '
            s+='\n'
            f.write(s)
        f.close()



    def pri(self):
        print('------')
        print(self.nBooks, self.nLibs, self.nDays)
        #print(self.libs)
        print('------')


if __name__ == "__main__":

    # p = Problem('data/a.txt')
    # p = Problem('data/b.txt')
    # p = Problem('data/c.txt')
    # p = Problem('data/d.txt')
    # p = Problem('data/e.txt')
    # p = Problem('data/f.txt')
    
    # p = Problem('data/a.txt')
    # solution = p.solve()
    # p.dump(solution)


    # p = Problem('data/b.txt')
    # solution = p.solve()
    # p.dump(solution)


    # p = Problem('data/c.txt')
    # solution = p.solve()
    # p.dump(solution)


    p = Problem('data/d.txt')
    solution = p.solve()
    p.dump(solution)


    # p = Problem('data/e.txt')
    # solution = p.solve()
    # p.dump(solution)


    # p = Problem('data/f.txt')
    # solution = p.solve()
    # p.dump(solution)
  