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

#affichage de l'automate
AF = lire_automate_sur_fichier(automate)
afficher_automate(AF)

#standardisation
#à compléter

#déterminisation et complétion
AFDC = test_determinisation_completion(AF)
#à compléter

#minimisation
AFDCM = minimisation(AFDC)
afficher_automate_minimal(AFDCM)

#reconnaissance de mots
#à compléter

#langage complémentaire
AComp = automate_complementaire(AFDC)
afficher_automate(AComp)