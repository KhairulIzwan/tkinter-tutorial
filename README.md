# tkinter-tutorial

## intro_1.py
- making a tkinter window

``` python
from tkinter import *
```
- import everything from tkinter

``` python
class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)               
        self.master = master
```
- master widget

``` python
root = Tk()
```
- Root window created

``` python
app = Window(root)
```
- create the instance

``` python
root.mainloop()
```
- show it and begin the mainloop

## intro_2.py
## intro_3.py
## intro_4.py
## intro_5.py
