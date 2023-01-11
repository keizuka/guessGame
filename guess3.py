import random
import datetime
mt = datetime.date.today().month# permet de verifier l'année en cours
yt = datetime.date.today().year# permet de verifier le mois en cours
année = yt
mois = mt
number = random.randrange(1,50)
ndc =  9
adn = int(input("votre année de naissance : "))# demande a l'utilisateur son année
mdn = int(input("votre mois de naissance : "))# demande a l'utilisateur son mois
age = année - adn # calcule l'age de l'utilisateur

while mdn != mois:# permet de verifier si le mois de naissance est sup ou inf au mois actuel
    if mdn >= mois:# permet de verifier si le mois et sup ou inf au mois de naissance 
        print("vous avez : ",age -1,"ans")
        break
    else:
        mdn <= mois
        print("vous avez : ",age,"ans")
        break
print("")
print("Et sans plus attendre un petit jeux tres simple")
guess = int(input("Devine le chiffre entre 1 et 50 : "))
print("")
while guess != number:
    if guess < number:# si le chiffre est inférieur
        print("plus ++")
        print("nombre de coup réstant : ",ndc)
        guess = int(input("\nRecomence : "))
    else:# et si le chiffre est superieur
        print("moins --")
        print("nombre de coup réstant : ",ndc)
        guess = int(input("\nRecomance : "))
    ndc = ndc -1
    if ndc == 0:# si perdu
        print("Perdu t'est vraiment une merde")   
        print("POINTS : Ba 0 t'est trop nul de toute façon")
        break
    if guess == number:# si gagner 
        print("yep ba bravo ta reussie a trouver un nombre tu peut être fière franchement c'est pas donner a tous le monde de réussir a trouvé un nombre donnée aléatoirement comme ca par un super programme qui envoie du paté du genre bien gras sa maman qui boie du sprite ...")
        print("ban ba voila aller casse toi")
        print("POINTS : ",ndc)
        break