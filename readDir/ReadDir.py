import os

class ReadDir:
    def __init__(self):
        self.isAlive = True

    def readDir(self, dirName):
        contents = os.listdir(dirName)
        wavList = []
        for val in contents:
            if val[-4:] == ".wav":
                wavList.append(val)
        return wavList
