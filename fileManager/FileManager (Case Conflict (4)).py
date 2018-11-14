# Farid Karadsheh
# 11/14/2018
# CIS 343

import os
from CLIAudioFileException.CLIAudioFileException import CLIAudioFileException


class FileManager:
    """Contains two methods that raise `CLIAudioFileException`s under certain circumstances."""

    def fileExists(self, filePath):
        """Raises an exception when a file does not exist."""
        if not os.path.exists(filePath):
            msg = "File: " + filePath + ", does not exist"
            raise CLIAudioFileException({filePath}, msg)

    def fileIsNotWav(self, filePath):
        """Raises an exception when a file is not a of `wav` format."""
    	if not filePath[-4:] == ".wav":
    		msg = "File: ", + filePath + ", is not a of wav format"
    		raise CLIAudioFileException({filePath}, msg)
