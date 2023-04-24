import tkinter

window=tkinter.Tk()

window.wm_attributes('-transparentcolor',"red")#1 прозрачность  2задать цвет прозрачности

label=tkinter.Label(window,text="ok",font=("Arial", 30),bg="red").place(x=0,y=0)







window.mainloop()
