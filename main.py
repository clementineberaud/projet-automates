from lire_automate import *
from affichage_automate import *
from standardisation import *
from determinisation import *
from minimisation import *
from reconnaissance import *
from complementaire import *

automate = ""

while automate != "stop" :
    #saisie de l'automate
    print("Quel automate voulez-vous tester ?")
    print("Pour arrêter le test, tapez 'stop'.")
    automate = input("Saisie : ")
    if automate == "stop" :
        break
    print()

    #affichage de l'automate
    print("Affichage de l'automate :")
    print()
    AF = lire_automate_sur_fichier(automate)
    afficher_automate(AF)
    print()
    print()

    #standardisation
    print("Standardisation :")
    print()
    AFS = est_standard(AF)
    afficher_automate(AFS)
    print()
    print()

    #déterminisation et complétion
    print("Déterminisation et complétion :")
    print()
    AFDC = determinisation_final(AF)
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
    print("Reconnaissance de mots : ")
    print()
    print("Pour arrêter les saisies, entrer 'fin'.")
    mot = input("Saisir un mot : ")
    while mot != "fin" :
        print(reconnaitre_mot(mot, AFDC))
        mot = input("Saisir un mot : ")
    print()
    print()

    #langage complémentaire
    print("Langage complémentaire :")
    print()
    AComp = automate_complementaire(AFDC)
    afficher_automate(AComp)
    print()
    print()