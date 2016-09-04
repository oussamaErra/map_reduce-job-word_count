#!/usr/local/bin/python

import sys
from itertools import groupby
from operator import itemgetter
sep='\t'
class reducer(object):
    def __init__(self,stream , sep = sep):
        self.stream = stream
        self.sep = sep
    def __iter__(self):
        for line in self.stream:
            try:
                parts = line.split(self.sep)
                yield parts[0] , float(parts[1])
            except:
                continue
    def emit(self , key , value):
        sys.stdout.write("%s%s%s\n"%(key,self.sep,value))
    def reduce(self):
        for word , numbr in groupby(self,itemgetter(0)):
            total = sum(int(x) for y , x in numbr)
            self.emit(word,total)

reduces = reducer(sys.stdin)
reduces.reduce()                       