#!/usr/bin/env python

'''
Basic of Tkinter -- Intro
'''
try:
    # Python 2
    from Tkinter import *

except ImportError:
    # Python 3
    from tkinter import *


class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master


root = Tk()
app = Window(root)
root.mainloop()
