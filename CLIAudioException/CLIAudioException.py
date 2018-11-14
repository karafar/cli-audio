# Farid Karadsheh
# 11/14/2018
# CIS 343

# https://www.codementor.io/sheena/how-to-write-python-custom-exceptions-du107ufv9
# All of the exception files were based on the blog post above.

class CLIAudioException(Exception):
    """Base class for audio exceptions. Not intended to be instantiated, i.e., abstract"""
    def __init__(self, dErrorArguments, msg):
        """
        Constructor
        :param dErrorArguments: Arguments used at time of error.
        :param msg: A message to to the user.
        """
        msg = msg + " \nRaised with arguments {0}"
        Exception.__init__(self, msg.format(dErrorArguments))
        self.dErrorArguments = dErrorArguments
