# coding=utf-8


class FileOperate:
    def __init__(self, path):
        self.path = path
        self.content = None
        self.readFile()

    def readFile(self):
        stream = open(self.path)
        self.content = stream.read()
        stream.close()

    def p(self):
        print "ss"


if __name__ == "__main__":
    pass
