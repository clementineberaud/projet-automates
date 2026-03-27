from lire_automate import *
from affichage_automate import *
from standardisation import *
from determinisation import *
from minimisation import *
from reconnaissance import *
from complementaire import *

#saisie de l'automate
print("Quel automate voulez-vous tester ?")
automate = input("Saisie : ")
print()

#affichage de l'automate
print("Affichage de l'automate :")
print()
AF = lire_automate_sur_fichier(automate)
afficher_automate(AF)
print()
print()

#standardisation
#à compléter

#déterminisation et complétion
print("Déterminisation et complétion :")
print()
AFDC = determinisation_final(AF)
#à compléter
print()
print()

#minimisation
print("Minimisation :")
print()
AFDCM = minimisation(AFDC)
print()
afficher_automate_minimal(AFDC, AFDCM)
print()
print()

#reconnaissance de mots
#à compléter

#langage complémentaire
print("Langage complémentaire :")
print()
AComp = automate_complementaire(AFDC)
afficher_automate(AComp)
print()
print()