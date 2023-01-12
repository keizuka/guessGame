import tkinter
from tkinter import *
import datetime
import random
year = datetime.date.year
month = datetime.date.month
def age():
    age:year-birthYear
def birthMonth():
    birthMonth==tkinter.Entry(app,)
app = tkinter.Tk()
app.title("guessing game")
app.iconbitmap("logo.ico")
app.minsize(600, 400)
label_welcome = tkinter.Label(app, text="Welcome to the guessing game", font=18)
label_welcome.pack()
label_info = tkinter.Label(app, text="We need some information about you,\n something like your year and month birth\n\n")
label_info.pack()
birthYear = tkinter.Entry (app, width=4) # année de naissance de l'utilisateur
birthYear.pack()
sauteLigne = tkinter.Label(app, text=("year"))
sauteLigne.pack()
birthMonth(type(int)) == tkinter.Entry(app, width=2) # mois de naissance de l'utilisateur
birthMonth.pack()
sauteLigne = tkinter.Label(app, text=("month"))
sauteLigne.pack()
sauteLigne = tkinter.Label(app, text=("\n"))
sauteLigne.pack()

while birthMonth!=month:
    if birthMonth(type(int))<month:
        age_label = tkinter.Label (age, text="years old")
        age_label.pack()
    else:
        birthMonth>=month
        age_label = tkinter.Label (age + 1, text="years old")        
button_calc = tkinter.Button(app, text="checking", width=7, height=2, command=age)
button_calc.pack()
sauteLigne = tkinter.Label(app, text=("\n"))
sauteLigne.pack()




app.mainloop()