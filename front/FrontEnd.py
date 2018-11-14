# Farid Karadsheh and Prof. Ira Woodring
# 11/14/2018
# CIS 343

import curses
import curses.textpad
from readDir.ReadDir import ReadDir
from library.Library import Library
from CLIAudioFileException.CLIAudioFileException import CLIAudioFileException
from CLIAudioScreenSizeException.CLIAudioScreenSizeException import CLIAudioScreenSizeException
from fileManager.FileManager import FileManager
import sys
import os

class FrontEnd:
    """The front end class acts as the standard screen for the curses subsystem. In addition,
        this class holds the responsibility of managing user input and delegating tasks 
        to various susbsystems.
    """

    def __init__(self, player):
        """
            Constructor: instatiates member variables and begins application with the
            curses wrapper function.

            :param player: Instatiated in __main__, holds the responsibility of playing .wav files.
        """
        self.player = player
        self.readDir = ReadDir()
        self.fileManager = FileManager()
        self.library = Library()
        curses.wrapper(self.menu)


    def menu(self, args):
        """
            The loop that resides here is the heart of the application. We perform an initial setup, and then
            continually poll for user input.

            :param args: Command line arguments passed in from __main__.
        """

        self.stdscr = curses.initscr()
        screenToSmall = True
        while screenToSmall:
            try:
                height, width = self.stdscr.getmaxyx()
                if height < 25 or width < 100:
                    raise CLIAudioScreenSizeException({height, width}, "Terminal window is too small.")
                screenToSmall = False
            except:
                self.stdscr.addstr(0, 0, "Enlarge terminal window!")
            finally:
                self.stdscr.refresh()
        curses.start_color()
        self.stdscr.keypad(1) 
        self.stdscr.addstr(0,0, "                          ")
        self.stdscr.addstr(0,0, "cli-audio",curses.A_REVERSE)
        self.stdscr.addstr(5,10, "c - Change current song")
        self.stdscr.addstr(6,10, "p - Play/Pause")
        self.stdscr.addstr(7,10, "l - Library")
        self.stdscr.addstr(9,10, "ESC - Quit")
        self.updateSong()
        self.stdscr.refresh()
        while True:
            c = self.stdscr.getch()
            if c == 27:
                self.quit()
            elif c == ord('p'):
                self.player.pause()
            elif c == ord('c'):
                self.changeSong()
                self.updateSong()
                self.stdscr.touchwin()
                self.stdscr.refresh()
            elif c == ord('l'):
                self.changeSong(self.library.library(self.stdscr, self.readDir.readDir("./media")))
                self.updateSong()
                self.stdscr.touchwin()
                self.stdscr.refresh()
             
    
    def updateSong(self):
        """Updates string that is shown on the screen."""
        self.stdscr.addstr(15,10, "                                        ")
        self.stdscr.addstr(15,10, "Now playing: " + self.player.getCurrentSong())


    def changeSong(self, song=None):
        if song == None:
            flag = True
            path = None
            while flag:
                try:
                    changeWindow = curses.newwin(5, 45, 5, 50)
                    changeWindow.border()
                    changeWindow.addstr(0,0, "What is the file path? Type 'exit' to exit", curses.A_REVERSE)
                    self.stdscr.refresh()
                    curses.echo()
                    path = changeWindow.getstr(1,1, 30)
                    curses.noecho()
                    if path == 'exit':
                        return
                    self.fileManager.fileExists(path)
                    self.fileManager.fileIsNotWav(path)
                    self.player.stop()
                    self.player.play(path.decode(encoding="utf-8"))
                    flag = False
                except:
                    self.player.currentSong = ("                                    ")
                    self.player.currentSong = "Unable to play, '" + path + "'"
                finally:
                    del changeWindow  
                    self.stdscr.refresh()
            self.stdscr.touchwin()
        else:
            self.player.stop()
            song = "./media/" + song
            try:
                self.fileManager.fileExists(song)
                self.fileManager.fileIsNotWav(song) 
                self.player.play( song.decode(encoding="utf-8") )
            except:
                self.player.currentSong = "Unable to play, '" + song + "'"
                return
              

    def quit(self):
        self.player.stop()
        exit()
