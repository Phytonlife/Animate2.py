import tkinter

map=[list("#"*12)]*12
print(*map,sep="\n")

Window= tkinter.Tk()
#buttons
for y in range(10):
    for x in range(10):
        button=tkinter.Button(Window,bd=2,width=4,height=2)
        button.place(x=x*10,y=y*10)










Window.mainloop()