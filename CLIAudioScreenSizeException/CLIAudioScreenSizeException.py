# Farid Karadsheh
# 11/14/2018
# CIS 343

from CLIAudioException.CLIAudioException import CLIAudioException

class CLIAudioScreenSizeException(CLIAudioException):
	"""Is thrown when the screen is too small."""
	def __init__(self, dErrorArguments, msg):
		"""
		Constructor
		:param dErrorArguments: A set of Arguments used at the time of error.
		:param msg: A message to the user.
		"""
		CLIAudioException.__init__(self,dErrorArguments, msg)
