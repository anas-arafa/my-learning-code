from random import random
from tkinter import *
win= Tk()
win.geometry("700x700")
message=Label(master=win, text="tic tac toe", font=("bold", 30))
message.pack()

message2= Label(master=win, text="RAEDY!!", font=("bold", 20))
message2.pack()

btn_frame=Frame(master=win)
btn_frame.pack()

bottons=[[0,0,0],
         [0,0,0],
         [0,0,0]]

for row in range(3):
    for col in range(3):
        bottons[row][col]=Button(master=btn_frame, text="", width=20, height=10)
        bottons[row][col].grid(row=row, column=col, padx=5, pady=5)


win.mainloop()