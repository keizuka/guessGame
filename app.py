
from tkinter import *

# premiere fenetre
rootWindow = Tk()
nextWindow = Tk()
# perso
rootWindow.title("guessing game")  # nom de la fenetre
rootWindow.geometry("400x600")  # taille de la fenetre
rootWindow.iconbitmap("logo.ico") # logo de l'app
rootWindow.config(background='#939393')  # couleur de fond
rootFrame = Frame(rootWindow, bg='#939393', bd=1,)
nextWindow.title("starting")
nextWindow.geometry("400x600")
nextWindow.iconbitmap("logo.ico")
nextWindow.config(background='#939393')
# ajout premier text
label_title = Label(rootWindow, text="welcome to the wheel of price", bg='#939393', fg='black', font=("Courrier", 18))  # bg=background fg=frontground
label_title.pack(pady=50)
label_subtitle = Label(rootWindow, text="just a simple rule don't be a dick", bg='#939393', fg='white', font=("Courrier", 10))
label_subtitle.pack()
# ajout du premier bouton
sartBouton = Button(rootWindow, text="Start", bg='white', fg='black', font=("Courrier", 18), command=exit, COMMAND=nextWindow)
sartBouton.pack(pady=25, fill=X, side=BOTTOM)
width = 300
height = 300
image = PhotoImage(file="a4e_cockpit_photo.png").zoom(10).subsample(32)
canvas = Canvas(rootWindow, width=width, height=height, bg='#939393', bd=0, highlightthickness=0)
canvas.create_image(width/2, height/2, image=image)
canvas.pack(expand=YES)
# afficher
rootWindow.mainloop()
