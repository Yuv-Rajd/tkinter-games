# import tkinter
# import tkinter as tk
# import random
# computer=random.randint(0,1)
# print(computer)
# window=tk.Tk()
# window.geometry('400x400')
# window.title("IN AND OUT GAME")
# lable=tkinter.Label(window,text="Enter your choice",width=50,font=("arial",12))
# lable.place(x=30,y=30)
# en= tkinter.Entry(window)
# en.place(x=100,y=100)

# canvas=tkinter.Canvas(width=700,height=700)
# canvas.create_rectangle(100,200,600,600,fill='blue')
# canvas['bg']='green'
# canvas.pack()

# player=canvas.create_oval(100,100,200,200,fill='pink')
# print("IN=0,OUT=1")
# user=int(input("enter your choice-"))
# print(user)

# def forward():
#     player1 = canvas.create_oval(200, 200, 300, 300, fill='pink')
#     canvas.delete(player)
# def backward():
#     player2=canvas.create_oval(100,100,200,200,fill='pink')
#     canvas.delete(player)

# def play(user):
#     count=0
#     if user==0:
#         if user==computer:
#             forward()
#             count +=1

#         else:
#             forward()

#     elif user==1:
#         if user==computer:
#             count+=1
#             backward()
#         else:
#             backward()
#     print("User score=",count)


# play(user)
# window.mainloop()
import random
import tkinter
import tkinter as tk

window_main = tk.Tk(className='Tkinter - TutorialKart', )
window_main.geometry("400x200")

entry_1 = tk.StringVar()

entry_widget_1 = tk.Entry(window_main, textvariable=entry_1)
entry_widget_1.pack()


def submitValues():
    global Value
    User=entry_1.get()
    print(User)
    Value=User
    Value.set(User)



submit = tk.Button(window_main, text="Submit", command=submitValues)
submit.pack()

computer = random.randint(0, 1)
print(computer)

canvas = tkinter.Canvas(width=700, height=700)
canvas.create_rectangle(100, 200, 600, 600, fill='blue')
canvas['bg'] = 'green'
canvas.pack()

player = canvas.create_oval(100, 100, 200, 200, fill='pink')
print("IN=0,OUT=1")


def forward():
    player1 = canvas.create_oval(200, 200, 300, 300, fill='pink')
    canvas.delete(player)


def backward():
    player2 = canvas.create_oval(100, 100, 200, 200, fill='pink')
    canvas.delete(player)


def play(user):
    count = 0
    if user == 0:
        if user == computer:
            forward()
            count += 1

        else:
            forward()

    elif user == 1:
        if user == computer:
            count += 1
            backward()
        else:
            backward()


play(Value)
window_main.mainloop()