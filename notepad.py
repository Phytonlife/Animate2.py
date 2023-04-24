import tkinter

map = [list("#" * 12)] * 12
print(*map, sep="\n")

Window = tkinter.Tk()

# buttons
for y1 in range(10):
    for x1 in range(10):
        button = tkinter.Button(Window, bd=2, width=10, height=5)
        button.place(x=x1 * 100+100, y=y1 * 100+50)

Window.mainloop()
