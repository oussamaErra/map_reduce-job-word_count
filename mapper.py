#!/usr/local/bin/python
import sys
import operator

sep='\t'
class mapper(object):
    def __init__(self, stream , sep=sep):
        self.stream = stream
	self.sep=sep
    def emit(self,key,value):
        sys.stdout.write('%s%s%s\n'%(key,self.sep,value))
    def mapps(self):
        for line in self.stream :
		line.strip()
		for word in line.split():
		
                 self.emit(word,1)
if __name__=='__main__':
    maper=mapper(sys.stdin)
    maper.mapps()