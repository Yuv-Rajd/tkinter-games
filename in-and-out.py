import tkinter
import tkinter as tk
import random
computer=random.randint(0,1)
print(computer)
window=tk.Tk()
window.geometry('400x400')
window.title("IN AND OUT GAME")
lable=tkinter.Label(window,text="Enter your choice",width=50,font=("arial",12))
lable.place(x=30,y=30)
en= tkinter.Entry(window)
en.place(x=100,y=100)

canvas=tkinter.Canvas(width=700,height=700)
canvas.create_rectangle(100,200,600,600,fill='blue')
canvas['bg']='green'
canvas.pack()

player=canvas.create_oval(100,100,200,200,fill='pink')
print("IN=0,OUT=1")
user=int(input("enter your choice-"))
print(user)

def forward():
    player1 = canvas.create_oval(200, 200, 300, 300, fill='pink')
    canvas.delete(player)
def backward():
    player2=canvas.create_oval(100,100,200,200,fill='pink')
    canvas.delete(player)

def play(user):
    count=0
    if user==0:
        if user==computer:
            forward()
            count +=1

        else:
            forward()

    elif user==1:
        if user==computer:
            count+=1
            backward()
        else:
            backward()
    print("User score=",count)


play(user)
window.mainloop()