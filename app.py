import tkinter
from tkinter import *
import datetime
import random
year = datetime.date.year
month = datetime.date.month
app = tkinter.Tk()
app.title("guessing game")
app.iconbitmap("logo.ico")
app.minsize(600, 400)
label_welcome = tkinter.Label(app, text="Welcome to the guessing game", font=18)
label_welcome.pack()
label_info = tkinter.Label(app, text="We need some information about you,\n something like your year and month birth\n\n")
label_info.pack()
birthYear = tkinter.Entry(width=4) # année de naissance de l'utilisateur
birthYear.pack()
sauteLigne = tkinter.Label(app, text=("year"))
sauteLigne.pack()
birthMonth = tkinter.Entry(width=2) # mois de naissance de l'utilisateur
birthMonth.pack()
sauteLigne = tkinter.Label(app, text=("month"))
sauteLigne.pack()
sauteLigne = tkinter.Label(app, text=("\n"))
sauteLigne.pack()
button_calc = tkinter.Button(app, text="checking", width=7, height=2)
button_calc.pack()
sauteLigne = tkinter.Label(app, text=("\n"))
sauteLigne.pack()
age_label = tkinter.Label(app)



app.mainloop()