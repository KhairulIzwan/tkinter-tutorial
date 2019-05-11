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
- create a button

``` python
def init_window(self):

      # changing the title of our master widget
      self.master.title("GUI")

      # allowing the widget to take the full space of the root window
      self.pack(fill=BOTH, expand=1)

      # creating a button instance
      quitButton = Button(self, text="Quit")

      # placing the button on my window
      quitButton.place(x=0, y=0)
```
## intro_3.py
- event handling

``` python
def client_exit(self):
      exit()
```

## intro_4.py
- menu bar

``` python
# creating a menu instance
menu = Menu(self.master)
self.master.config(menu=menu)

# create the file object)
file = Menu(menu)

# adds a command to the menu option, calling it exit, and the
# command it runs on event is client_exit
file.add_command(label="Exit", command=self.client_exit)

#added "file" to our menu
menu.add_cascade(label="File", menu=file)

# create the file object)
edit = Menu(menu)

# adds a command to the menu option, calling it exit, and the
# command it runs on event is client_exit
edit.add_command(label="Undo")

#added "file" to our menu
menu.add_cascade(label="Edit", menu=edit)
```
## intro_5.py
- image and text

``` python
# create the file object)
edit = Menu(menu)

# adds a command to the menu option, calling it exit, and the
# command it runs on event is client_exit
edit.add_command(label="Show Img", command=self.showImg)
edit.add_command(label="Show Text", command=self.showText)

#added "file" to our menu
menu.add_cascade(label="Edit", menu=edit)
```
