from CLIAudioException.CLIAudioException import CLIAudioException

class CLIAudioFileException(CLIAudioException):
    """Is thrown when a file cannot be played."""
    def __init__(self, dErrorArguments, msg):
        """
        Constructor
        :param dErrorArguments: Arguments used at time of error.
        :param msg: An erroneous path to a file.
        """
        CLIAudioException.__init__(self, dErrorArguments, msg)

