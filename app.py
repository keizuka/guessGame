
from tkinter import *

# premiere fenetre
rootWindow = Tk()
# perso
rootWindow.title("guessing game")  # nom de la fenetre
rootWindow.geometry("600x600")  # taille de la fenetre
rootWindow.iconbitmap("logo.ico") # logo de l'app
rootWindow.config(background='#939393')  # couleur de fond
rootFrame = Frame(rootWindow, bg='#939393', bd=1,)
# ajout premier text
label_title = Label(rootWindow, text="welcome to the wheel of price", bg='#939393', fg='black', font=("Courrier", 18))  # bg=background fg=frontground
label_title.pack()
label_subtitle = Label(rootWindow, text="just a simple rule don't be a dick", bg='#939393', fg='white', font=("Courrier", 10))
label_subtitle.pack()
# afficher
rootWindow.mainloop()
