def afficher_automate(automate):
    alphabet = automate["alphabet"]
    etats = automate["etats"]
    initiaux = automate["initiaux"]
    finaux = automate["finaux"]
    transitions = automate["transitions"]

    print("Alphabet :", alphabet)
    print("Etats :", etats)
    print("Etats initiaux :", initiaux)
    print("Etats finaux :", finaux)
    print()


    entete = [" "] + ["Etat"] + alphabet
    largeurs = []

    calculer les tailles
    tableau = []
    tableau.append(entete)

    for etat in etats:
        marque = " "
        if etat in initiaux and etat in finaux:
            marque = "I/F"
        elif etat in initiaux:
            marque = "I"
        elif etat in finaux:
            marque = "F"

