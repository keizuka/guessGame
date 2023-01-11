import tkinter
from tkinter import *
app = tkinter.Tk()
app.title("The guessing game")
app.maxsize(600, 400)
app.minsize(600, 400)
app.iconbitmap("logo.ico")
app.config(background='#939393')

label_welcome = tkinter.Label(app, text="welcome to the guessing game\n i hope you enjoy it", bg='#939393', fg='black', font=("Courrier", 18))
label_welcome.pack()
label_info = tkinter.Label(app, text="please enter your year an mounth birth for verify your age\n thank's\n",)
entry_year = tkinter.Entry(app, width=4)
entry_mounth = tkinter.Entry(app, width=2)
appFrame = Frame(app, entry_mounth)
#appFrame = Frame(app, entry_year)
entry_year.pack()
entry_mounth.pack()

app.mainloop()