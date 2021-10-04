class XMLParse(object):

    def __init__(self, input):
        self.stmt = ""
        self.input = input

    def advance(self):
        self.input = self.input[1:]
        return
    
    def readOne(self, c):
        return self.input[0].find(c)

    def read(self, c, i):
        return self.input[0][i + 1:].find(c)

    def readStmt(self):
        return self.stmt

    def parseRoot(self):
        self.input = self.input[1:-1]
        return self.parseEle()

    def parseGen(self):
        i = self.readOne(">") + 1
        j = self.read("<", i) - 1
        self.stmt += self.input[0][i:j]
        return

    def parseAttr(self):
        self.advance()
        i = self.readOne("")
        j = self.readOne(">") - 1
        self.stmt += self.input[0][i:j] + ','
        i = self.readOne(">") + 1
        j = self.readOne("<") - 1
        self.stmt += '"' + self.input[0][i:j] + '",'
        return

    def parseDesc(self):
        end = '</description>'
        self.stmt += '"'
        while (self.input[0] is not end):
            self.advance()
            self.stmt += self.input[0] + ' '
        self.stmt += '",'
        return

    def parseEntry(self, start):
        if not self.input:
            return
        end = self.input[-1]
        while self.input[0] != end:
            self.advance()
            #print(['test', self.input])
            if '=' in self.input[0]:
                self.parseAttr()
            elif self.input[0] is '<description>':
                self.parseDesc()
            else:
                self.parseGen()
        self.stmt += ');\n'
        self.advance()
        if not self.input:
            self.parseEle()
        return

    def parseEle(self):
        start = self.input[0][1:-1]
        self.stmt += 'INSERT INTO ' + start + ' VALUES ('
        return self.parseEntry(start)

    def parse(self):
        if self.input is None:
            raise Exception("Empty XML File.")
        return self.parseRoot()
