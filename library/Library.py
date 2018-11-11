#!/usr/bin/python
import curses
from curses import wrapper
from readDir.ReadDir import ReadDir
from math import ceil

# def main(stdscr):
# 	curses.noecho()
# 	curses.cbreak()
# 	stdscr.keypad(1)
# 	curses.start_color()
# 	#curses.init_pair(1,curses.COLOR_BLACK, curses.COLOR_CYAN)
# 	#highlightText = curses.color_pair(1)
# 	normalText = curses.A_NORMAL
# 	stdscr.addstr(5,5, "Hello!", normalText)
# 	library(stdscr)
# 	stdscr.refresh()
# #	stdscr.getch()

class Library:

	# def __init__(self):


	def library(self, stdscr, media):
		# Set up colors
		curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_CYAN)
		highlightText = curses.color_pair(1)
		normalText = curses.A_NORMAL
		# Read the media folder
		readDir = ReadDir()
		media = readDir.readDir("./media/")
		# Create new window and paginator
		maxRows = 20
		numRows = len(media)
		# We cast as floats to prevent a truncation prior to ceil()
		numPages = int( ceil(float(numRows)/float(maxRows)) )
		position = 0
		page = 1
		libraryWindow = curses.newwin(maxRows + 2, 20, 5, 35)
		libraryWindow.box()
		# We populate the libraryWindow with the contents of media
		for i in range(0, maxRows):
			y = i + 1 # Used to offset the strings

			# Notify the user that the library empty
			if numRows == 0: 
				libraryWindow.addstr(y, 1, "Your library is empty!", highlightText)
			else:
				# Highlight the first option
				if(i == position):
					libraryWindow.addstr(y, 1, media[i], highlightText)
				# Add the remaining strings
				else:
					libraryWindow.addstr(y, 1, media[i], normalText)
				# This happens when the list is smaller than the max number of rows,
				# i.e., numRows < maxRows
				if i == (numRows-1):
					break
		stdscr.refresh()
		libraryWindow.refresh()
		# We continually populate the elements to the window and wait for user input.
		# The user input is used for traversing the list.
		c = stdscr.getch()
		# 27 is the keycode for escape
		while c != 27:

			if c == curses.KEY_DOWN:
				# The last row on the last page. If only one page exists, it is the last page 
				if page == numPages:
					if position < numRows - 1: 
						position += 1
				# The last row on a page
				elif (position == (page * maxRows) - 1):	
			 		page += 1
					position += 1
				# On any given page, but not at the bottom row
				else:
					position += 1

			if c == curses.KEY_UP:
				# First page, do not show previous page
				if page == 1:
					if position > 0:
						position -= 1
				# At the top row of a page, show previous page
				elif (position == (page - 1) * maxRows):
					page -= 1
					position -= 1
				# On any given page, but not at the top row
				else:
					position -= 1

			if c == ord("\n"):
					return media[position]

			libraryWindow.erase()
			libraryWindow.box()

			# Repopulate the list, and add highlighting to selected row
			for i in range( maxRows * (page - 1), (maxRows * page)):
				if numRows == 0:
					libraryWindow.addstr(0, 1, "You're library is empty", hightlightText)
				else:
					y = i - (maxRows * (page - 1)) + 1

					if i == (numRows):
						break
					if i == position:
						libraryWindow.addstr(y, 1, media[i], highlightText)
					else:
						libraryWindow.addstr(y, 1, media[i], normalText)
		
			stdscr.refresh()	
			libraryWindow.refresh()
			c = stdscr.getch()
