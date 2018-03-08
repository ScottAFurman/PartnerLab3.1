# Partner Lab 3.1 - Class Interactions (ComicBook Class)
# Authors: Scott Furman and Adrian Michniewicz
# Class: Programming Two - Period 04
# Last Modified: March 8th, 2018

from Book import *

class ComicBook(Book):
    """Creates a single comic book object"""

    def __init__(self, x, y, color, win):
        super(ComicBook, self).__init__(x, y, color, win)
        ##self.drawTitle(win)
        self.drawLogo(win)
        ##self.drawAuthor(win)
        ##self.drawChapter(win)

    def drawLogo(self, win):
        logo = Oval(Point(self.x, self.y + 25), Point(self.x + 25, self.y + 25))
        logo.setFill("gray")
        logo.draw(win)
