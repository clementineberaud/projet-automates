from lire_automate import *
from determinisation import *
from affichage_automate import *
automate=input("Quel automate voulez-vous tester ?")
a=lire_automate_sur_fichier(automate)
print(a)


afficher_automate_deterministe_complet(a)
