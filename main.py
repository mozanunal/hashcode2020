
from library import Library, Book
import numpy as np

class Problem(object):
    def __init__(self, filename):
        f = open(filename)
        l = f.readline().split(' ')
        self.filename = filename
        self.nBooks, self.nLibs, self.nDays = int(l[0]), int(l[1]), int(l[2])
        self.books = [ Book(i,int(score)) for i, score in enumerate(f.readline().split(' '))]
        self.book2Score = {book.id: int(book.score) for book in self.books}
        self.libs = []
        for i in range(self.nLibs):
            l = [int(i) for i in f.readline().split(' ')]
            nBooks, nSign, nScan = l[0], l[1], l[2]
            books = [ Book(int(i), int(self.book2Score[int(i)])) for i in f.readline().split(' ') ] 
            lib = Library(i, nBooks, nSign, nScan, books)
            self.libs.append(lib) 
        self.pri()

    def solve(self):
        t = 0
        solution = []
        readBookSet  = set()
        while t < self.nDays:
            scoreList = []
            for lib in self.libs:
                if lib.registered == False:
                    scoreList.append(
                        lib.predMaxScore(self.nDays - t) 
                    )
                else:
                    scoreList.append(0)
            if len(scoreList) == 0:
                break
            if max(scoreList) == 0:
                break
            libIndex = scoreList.index(max(scoreList))
            self.libs[libIndex].registeredDay = t
            self.libs[libIndex].registered = True
            solution.append(self.libs[libIndex])
            t += self.libs[libIndex].nSign
        print([(lib.id, lib.nSign, lib.registeredDay) for lib in solution])
        return solution

    def dump(self, solution):
        f = open(self.filename.replace('data/', 'out/'), 'w+')
        f.write('{}\n'.format(len(solution)))
        for lib in solution:
            books = lib.getSol(self.nDays)
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
    
    p = Problem('data/a.txt')
    solution = p.solve()
    p.dump(solution)


    # p = Problem('data/b.txt')
    # solution = p.solve()
    # p.dump(solution)


    # p = Problem('data/c.txt')
    # solution = p.solve()
    # p.dump(solution)


    # p = Problem('data/d.txt')
    # solution = p.solve()
    # p.dump(solution)


    # p = Problem('data/e.txt')
    # solution = p.solve()
    # p.dump(solution)


    p = Problem('data/f.txt')
    solution = p.solve()
    p.dump(solution)
    #p = Problem('data/b.txt')
    #p = Problem('data/c.txt')
    #p = Problem('data/d.txt')
    
    #solve()