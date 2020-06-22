import threading
import time

class rangeplus:
    sum = 0
    def __init__(self, range):
        self.range = range

    def plus(self):
        for i in range(1,self.range):
            self.sum += i
            stri = str(i)
            sumstr = stri + '+'
            print(sumstr, end='')
        self.sum += self.range
        print(self.range, "=", self.sum)

a = rangeplus(100)
b = rangeplus(1000)
c = rangeplus(10000)

th1 = threading.Thread(target = a.plus())
th2 = threading.Thread(target = b.plus())
th3 = threading.Thread(target = c.plus())

th1.start()
th2.start()
th3.start()