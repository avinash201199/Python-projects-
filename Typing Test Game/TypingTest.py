from words import words
from tkinter import *
import random
from tkinter import messagebox

Mainscreen= Tk()
Mainscreen.geometry('800x600')
Mainscreen.title('Typing Test')
Mainscreen.config(bg="#076BF6")

score=0
missed=0
time=60
count1=0
movingwords=''

def movingtext():
    global count1,movingwords
    floatingtext='Typing Test'
    if count1>= len(floatingtext):
        count1 =0
        movingwords =''
    movingwords += floatingtext[count1]
    count1 +=1
    fontlabel.configure(text=movingwords)
    fontlabel.after(150,movingtext)


def giventime():
    global time,score,missed
    if time>11:
        pass
    else:
        timercount.configure(fg='red')
    if time>0:
        time -=1
        timercount.configure(text=time)
        timercount.after(1000,giventime)
    else:
        gameinstruction.configure(text='Hit = {} | Miss = {} | Total Score = {}'
                                  .format(score,missed,score-missed))
        rr= messagebox.askretrycancel('Notification','Do you want to play again?')
        if rr==True:
            score=0
            missed=0
            time=60
            timercount.configure(text=time)
            labelforward.configure(text=words[0])
            scorelabelcount.configure(text=score)
            wordentry.delete(0, END)

def game(event):
    global score, missed
    if time==60:
        giventime()
    gameinstruction.configure(text='')
    startlabel.configure(text='')
    if wordentry.get()== labelforward['text']:
        score +=1
        scorelabelcount.configure(text=score)
    else:
        missed +=1
    random.shuffle(words)
    labelforward.configure(text=words[0])
    wordentry.delete(0,END)

fontlabel=Label(Mainscreen,text='',font=('arial',25,
                'italic bold'),fg='purple',width=40)
fontlabel.place(x=10,y=10)
movingtext()

startlabel=Label(Mainscreen,text='Start Typing',font=('arial',30,
                  'italic bold'),bg='black',fg='white')
startlabel.place(x=275,y=50)

random.shuffle(words)
labelforward=Label(Mainscreen,text=words[0],font=('arial',45,
                'italic bold'),fg='green')
labelforward.place(x=250,y=240)


scorelabel=Label(Mainscreen,text='Your Score:',font=('arial',25,
                'italic bold'),fg='red')
scorelabel.place(x=10,y=100)

scorelabelcount=Label(Mainscreen,text=score,font=('arial',25,
                'italic bold'),fg='blue')
scorelabelcount.place(x=150,y=180)



labelfortimer=Label(Mainscreen,text='Time Left:',font=('arial',25,
                'italic bold'),fg='red')
labelfortimer.place(x=600,y=100)

timercount=Label(Mainscreen,text=time,font=('arial',25,
                'italic bold'),fg='blue')
timercount.place(x=600,y=180)



gameinstruction= Label(Mainscreen,text='Hit enter button after typing the word',
                       font=('arial',25,'italic bold'),fg='grey')
gameinstruction.place(x=150,y=500)

wordentry= Entry(Mainscreen,font=('arial',25,'italic bold'),bd=10,justify='center')
wordentry.place(x=250,y=330)
wordentry.focus_set()

Mainscreen.bind('<Return>',game)
mainloop() 
