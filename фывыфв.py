    import tkinter
import random
from tkinter import messagebox
window = tkinter.Tk()
window.title('Word pick')
window.geometry('450x700')
window.configure(bg='white')
questions= [['what is the first routine you start with in rhythmic gymnastics', 'freehand'],['what animal do you call the king of the jungle', 'lion']]
question= random.choice(questions)
mainquestion=(question[0])
answer=(question[1])
def newgame ():
   global points
   points= 100
   entrylist = [window2, window3, window4, window5, window6, window7, window8, window9, window10]
   for element in entrylist:
       element.delete(0, 'end')
   text8['text']= points
   text5['text']= ''
   questions = [['what is the first routine you start with in rhythmic gymnastics', 'freehand'], ['what animal do you call the king of the jungle', 'lion']]
   question = random.choice(questions)
   global mainquestion
   global answer
   mainquestion = (question[0])
   answer = (question[1])
   text4['text']= mainquestion
def go():
   l1=(window1.get())
   if l1 in answer:
       global points
       points= points+random.randint(1,100)
       text8['text']= points
       text5['text']= 'You picked the right one'
       s= 0
       entrylist= [window2, window3, window4, window5, window6, window7, window8, window9, window10]
       for element in answer:
           s= s+1
           if l1 == element:
               entrywindow= entrylist[s-1]
               entrywindow.insert(0,element)
   else:
       points= points-random.randint(1,100)
       text8['text']= points
       text5['text']= 'Not the right one'
       if points <= 0:
           if messagebox.askokcancel('You have lost this game, you can either start again or exit'):
               newgame()
           else:
               window.destroy()
# gummyim= tkinter.PhotoImage(file=  'hot-pink-gummy-bear-modern-art-erin-kiser-transparent.png')
# gummyim= gummyim.subsample(1,1)
# text0= tkinter.Label(window, image= gummyim)
# text0.place(x=0, y=0)
text1=tkinter.Label(window, text= 'Word Pick Game', font=('Georgia', 30))
text1.place(x= 115, y= 10)
text2=tkinter.Label(window, text= 'pick your letter')
text2.place(x=10, y=380)
text3=tkinter.Label(window, text= 'Your word')
text3.place(x= 170, y=60)
text4=tkinter.Label(window, text= mainquestion, font=('Georgia', 16))
text4.place(x=40, y= 130)
text5=tkinter.Label(window, text= 'game status')
text5.place(x=40,y=230)
text6=tkinter.Label(window, text= 'Points', font=('Georgia', 16))
text6.place(x= 5, y= 5)
points= 100
text8=tkinter.Label(window, text= points, font= ('Georgia', 16))
text8.place(x=10, y=27)
window1=tkinter.Entry(window, font= ('Georgia', 17))
window1.place(x=10, y=400)
window2=tkinter.Entry(window, width= 3)
window2.place(x= 10, y=85)
window3=tkinter.Entry(window, width= 3)
window3.place(x= 60, y=85)
window4=tkinter.Entry(window, width= 3)
window4.place(x= 110, y=85)
window5=tkinter.Entry(window, width= 3)
window5.place(x= 160, y=85)
window6=tkinter.Entry(window, width= 3)
window6.place(x= 210, y=85)
window7=tkinter.Entry(window, width= 3)
window7.place(x= 260, y=85)
window8=tkinter.Entry(window, width= 3)
window8.place(x= 310, y=85)
window9=tkinter.Entry(window, width= 3)
window9.place(x= 360, y=85)
window10=tkinter.Entry(window, width= 3)
window10.place(x= 410, y=85)

# goim= tkinter.PhotoImage(file= 'img_3.png')
# goim= goim.subsample(9,9)
button1=tkinter.Button(window, text="enter", command= go)
button1.place(x=10, y= 440)
window.mainloop()