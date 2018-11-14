import os
from CLIAudioFileException.CLIAudioFileException import CLIAudioFileException


class FileManager:

    # def __init__(self):
    #     return

    def fileExists(self, filePath):
        if not os.path.exists(filePath):
            msg = "File: " + filePath + ", does not exist"
            raise CLIAudioFileException({filePath}, msg)

    def fileIsNotWav(self, filePath):
    	if not filePath[-4:] == ".wav":
    		msg = "File: ", + filePath + ", is not a of wav format"
    		raise CLIAudioFileException({filePath}, msg)
