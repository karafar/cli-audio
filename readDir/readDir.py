import os

class readDir:
	def __init__(self):
		self.isAlive = true

	def readDir(dirName):
		contents = os.listdir("./media")
		wavList = []
		for val in contents:
			if val[-4:] == ".wav":
				wavList.append(val)
		return wavList
