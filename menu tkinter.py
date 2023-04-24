from tkinter import *


class tiger:
    def __init__(self):
        self.tk = Tk()

        self.menu = Menu(self.tk, font='Helvetica 50 bold')  # no effect
        self.tk.config(menu=self.menu)

        self.main_menu = Menu(self.menu, tearoff=0, font='Helvetica 50 bold')  # no effect

        self.menu.add_cascade(label="Main", menu=self.main_menu, font='Helvetica 50 bold')
        self.main_menu.add_command(label="StartScreen", font='Helvetica 25 bold')
        self.main_menu.add_command(label="Settings", font='Helvetica 25 bold')
        self.main_menu.add_command(label="Exit", font='Helvetica 25 bold')

        # self.file.add_command = (font = 'Helvetica 12 bold')

        self.file_menu = Menu(self.menu, tearoff=0, font='Helvetica 50 bold')  # no ettect
        self.file_menu.add_command(label="Open", font='Helvetica 25 bold')
        self.file_menu.add_command(label="Save", font='Helvetica 25 bold')
        self.file_menu.add_command(label="Print", font='Helvetica 25 bold')
        self.menu.add_cascade(label="File", menu=self.file_menu)

        self.test_menu = Menu(self.menu, tearoff=0, font='Helvetica 50 bold')  # no effect
        self.test_menu.add_command(label="Test")
        self.menu.add_cascade(label="Test", menu=self.test_menu)


tiger()

mainloop()