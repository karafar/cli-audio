import curses
import curses.textpad
from readDir.ReadDir import ReadDir
from library.Library import Library
import sys

class FrontEnd:

    def __init__(self, player):
        self.player = player
        self.player.play(sys.argv[1])
        self.readDir = ReadDir()
        self.library = Library()
        curses.wrapper(self.menu)

    def menu(self, args):
        self.stdscr = curses.initscr()
        curses.start_color()
        self.stdscr.keypad(1) 
        self.stdscr.border()
        self.stdscr.addstr(0,0, "cli-audio",curses.A_REVERSE)
        self.stdscr.addstr(5,10, "c - Change current song")
        self.stdscr.addstr(6,10, "p - Play/Pause")
        self.stdscr.addstr(7,10, "l - Library")
        self.stdscr.addstr(9,10, "ESC - Quit")
        self.updateSong()
        self.stdscr.refresh()
        while True:
            c = self.stdscr.getch()
            # if self.libraryFlag:
                # self.library()
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
                # if self.libraryFlag:
                #     self.libraryFlag = False
                # else:
                #     self.libraryFlag = True
             
    
    def updateSong(self):
        self.stdscr.addstr(15,10, "                                        ")
        self.stdscr.addstr(15,10, "Now playing: " + self.player.getCurrentSong())

    def changeSong(self, song=None):
        if song == None:
            changeWindow = curses.newwin(5, 40, 5, 50)
            changeWindow.border()
            changeWindow.addstr(0,0, "What is the file path?", curses.A_REVERSE)
            self.stdscr.refresh()
            curses.echo()
            path = changeWindow.getstr(1,1, 30)
            curses.noecho()
            del changeWindow
            self.stdscr.touchwin()
            self.stdscr.refresh()
            self.player.stop()
            self.player.play(path.decode(encoding="utf-8"))
        else:
            self.player.stop()
            self.player.play( ("media/" + song).decode(encoding="utf-8") )
    
    # def library(self):
    #     contents = self.readDir.readDir("./media")
    #     y = 5
    #     self.stdscr.addstr(y, 100, "Library-------------------")
    #     for val in contents:
    #         y+=1
    #         self.stdscr.addstr(y, 100, val)
    #     self.stdscr.refresh()
    # def library(self):
    #     changeWindow = curses.newwin(50, 50, 5, 50)
    #     # changeWindow.border()
    #     y = 2
    #     changeWindow.addstr(0,0, "Library", curses.A_REVERSE)
    #     # y += 1
    #     # changeWindow.addstr(y,2, "----------------", curses.A_REVERSE)
    #     contents = self.readDir.readDir("./media")
        
    #     for val in contents:
    #         y+=1
    #         changeWindow.addstr(y, 2, val, curses.A_REVERSE)

    #     path = changeWindow.getstr(1,1, 30)
            
        

    def quit(self):
        self.player.stop()
        exit()
