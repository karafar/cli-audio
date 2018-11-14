# Farid Karadsheh
# 11/14/2018
# CIS 343

from CLIAudioException.CLIAudioException import CLIAudioException

class CLIAudioFileException(CLIAudioException):
    """Is thrown when a file cannot be played."""
    def __init__(self, dErrorArguments, msg):
        """
        Constructor
        :param dErrorArguments: Arguments used at time of error.
        :param msg: A messsage to the user.
        """
        CLIAudioException.__init__(self, dErrorArguments, msg)

