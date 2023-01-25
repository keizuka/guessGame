from tkinter import *
import datetime
import math
yt = datetime.date.year
mt = datetime.date.month
app = Tk()
app.title("guessing game")
app.iconbitmap("logo.ico")
app.minsize(600, 400)
label_welcome = Label(app, text="Welcome to guessing game\n")
label_welcome.pack()
label_welcome2 = Label(app, text="in first we need some information\n")
label_welcome2.pack()
year = IntVar
birthyear = int(input())(app, textvariable=year)
birthyear.pack()
age = yt-birthyear
yearlabel = Label(app, age)
yearlabel.pack()
def function():
    yearlabel['text'] = year.get()

bouton = Button(app, text="click me!!", command=function)
bouton.pack()

app.mainloop()