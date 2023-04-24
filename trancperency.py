import tkinter
import tkinter as tk

root = tk.Tk()
root.title('background image')

image1 = tk.PhotoImage(file="background.png")
# get the image size
w = image1.width()
h = image1.height()

# make the root window the size of the image
root.geometry("%dx%d" % (w, h)) # размер картинки под размер окна

# root has no image argument, so use a label as a panel
panel1 = tk.Label(root, image=image1)
panel1.grid(row=8,column=0,sticky=tkinter.N)
root.resizable(0,0)


#b=tkinter.Button(root,text="ok",width=40,height=2).grid(row=8,column=0,sticky=tkinter.S+tkinter.N+tkinter.E+tkinter.W,padx=50,pady=5)



# start the event loop
root.mainloop()