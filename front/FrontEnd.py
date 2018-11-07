import curses
import curses.textpad
from readDir.ReadDir import ReadDir
import sys

class FrontEnd:

    def __init__(self, player):
        self.player = player
        #self.player.play(sys.argv[1])
        self.readDir = ReadDir()
        curses.wrapper(self.menu)

    def menu(self, args):
        self.stdscr = curses.initscr()
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
            if c == 27:
                self.quit()
            elif c == ord('p'):
                self.player.pause()
            elif c == ord('c'):
                self.changeSong()
                self.updateSong()
                self.stdscr.touchwin()
                self.stdscr.refresh()
            elif c == ord("l"):
              # print("hello")
               self.library()
	                      
    
    def updateSong(self):
        self.stdscr.addstr(15,10, "                                        ")
        self.stdscr.addstr(15,10, "Now playing: " + self.player.getCurrentSong())

    def changeSong(self):
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
	
    def library(self):
        libraryWindow = curses.newwin(5, 40, 5, 50)
        libraryWindow.border()
        self.stdscr.refresh()
        self.stdscr.touchwin()
        contents = self.readDir.readDir("./media")
        y = 0
        for val in contents:
            #changeWindow.addstr(0, y, val, curses.A_REVERSE)
            y+=2
        #elf.stdscr.refresh()
        #elf.stdscr.touchwin()
        #self.stdscr.refresh()

    def quit(self):
        self.player.stop()
        exit()
