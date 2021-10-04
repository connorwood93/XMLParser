import re
import xmlparse as xp

class Store(object):

    def __init__(self, file):
        self.input = file

    def start(self):
        f = open(self.input, 'r')
        elem = f.read()
        input = re.sub('[$], '', elem').split()
        xmlp = xp.XMLParse(input[3:])
        xmlp.parse()
        return


f = open('test.xml', 'r')
elem = f.read()
input = re.sub('[$]', '', elem).split()
start = xp.XMLParse(input[3:])
output = start.parse()
print(start.readStmt())