from tkinter import *
win = Tk()
win.title("log in window")
win.geometry("500x500")
TF= Frame(master=win)
TF.pack()
message=Label(master=TF,text="facebook",fg="blue",font=("bold",40))
message.pack()
info=Frame(master=win)
info.pack()

username=Label(master=info,text="username",font=("bold",20))
username.grid(row=0,column=0)

ent_1 = Entry(master=info)
ent_1.grid(row=0,column=1)

password=Label(master=info,text="password",font=("bold",20))
password.grid(row=1,column=0)

ent_2=Entry(master=info)
ent_2.grid(row=1,column=1)

btn=Button(text="log in",width=10)
btn.pack(pady=10,ipady=10)
win.mainloop()