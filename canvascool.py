import tkinter
from tkinter import *
import webbrowser
root = Tk()

root.geometry("500x500")
def matem():
    webbrowser.open("https://google.com", new=0, autoraise=True)


b=Tk()
b.geometry("300x300+200+200")
button=tkinter.Button(root,command=matem).place(x=200,y=200)
root.mainloop()