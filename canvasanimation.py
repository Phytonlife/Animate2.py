from tkinter import *
import pygame

pygame.mixer.init()

def motion():
    c.move(ball, 2, 0)
    if c.coords(ball)[2] < 300: 
        root.after(10, motion)
def audio(event):  #Добовляем звуки
    pygame.mixer.music.load("../pythonProject3/car_pass_over_speed_bump_20kph_30548.mp3")
    pygame.mixer.music.play(loops=0)
    motion()


root = Tk()

c = Canvas(root, width=300, height=200,
           bg="white")
c.pack()
ball = c.create_oval(0, 100, 40, 140,
                     fill='green')
line=c.create_line(0,140,300,140, fill="black")

root.bind("<Return>",audio)
root.mainloop()