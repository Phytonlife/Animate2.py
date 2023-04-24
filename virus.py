import tkinter
import random
import time
window=tkinter.Tk()
window.title('virus.exe')
a=0
def virus():
    global a
    a=a+1

    if a%20==0:
        a=0
        window = tkinter.Tk()
        window.geometry(f"{random.randint(1,2000)}x{random.randint(1,2000)}+{random.randint(1,2000)}+{random.randint(1,2000)}")
        window.wm_attributes("-topmost",1)
    virus()





button=tkinter.Button(window,text="open.noob",font=('Arial',50),bd=15,command=virus).pack()






































window.mainloop()
