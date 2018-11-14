# Farid Karadsheh
# 11/14/2018
# CIS 343

import os

class ReadDir:
	"""Simple class for reading in the `wav` files within the directory."""

    def readDir(self, dirName):
    	"""Reads a directory, if the has the `wav` extension then said file is added 
    	to a list.
		:return wavlist: The list of `wav` files within the directory.
    	"""
        contents = os.listdir(dirName)
        wavList = []
        for val in contents:
            if val[-4:] == ".wav":
                wavList.append(val)
        return wavList
