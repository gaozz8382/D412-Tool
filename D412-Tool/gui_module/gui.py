#!/usr/bin/env python3
#-*- coding:utf-8 -*-

from tkinter import *
import tkinter.messagebox as messagebox

# def gui_start():
#     init_window = Tk()
#     init_window.mainloop()

# gui_start()

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.alertButton = Button(self, text='START', command=self.hello)
        self.alertButton.pack()
    
    def hello(self):
        # name = self.nameInput.get() or 'world'
        name = 'world'
        messagebox.showinfo('Message', 'Hello, %s' % name)

# 
app = Application()
# set window title：
app.master.title('D412-Tool')
app.createWidgets()

# main fuction
if __name__ == '__main__':
    app.mainloop()