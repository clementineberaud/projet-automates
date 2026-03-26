def afficher_automate(a):
    # affichage des informations principales de l'automate
    print("Alphabet :", a["alphabet"])
    print("Etats :", a["etats"])
    print("Initial :", a["initial"])
    print("Final :", a["final"])
    print()

    # création du tableau
    tableau = []

    # en-tête du tableau
    entete = ["Type", "Etat"]
    for lettre in a["alphabet"]:
        entete.append(str(lettre))
    tableau.append(entete)

    # création des lignes du tableau
    for etat in a["etats"]:
        if etat in a["initial"] and etat in a["final"]:
            type_etat = "E/S"
        elif etat in a["initial"]:
            type_etat = "E"
        elif etat in a["final"]:
            type_etat = "S"
        else:
            type_etat = ""

        ligne = [type_etat, str(etat)]

        # remplissage des transitions
        for lettre in a["alphabet"]:
            texte = "--"

            if etat in a["transitions"]:
                if lettre in a["transitions"][etat]:
                    dest = a["transitions"][etat][lettre]

                    if dest == []:
                        texte = "--"
                    else:
                        texte = ""
                        for i in range(len(dest)):
                            texte += str(dest[i])
                            if i != len(dest) - 1:
                                texte += ","

            ligne.append(texte)

        tableau.append(ligne)

    # calcul de la largeur des colonnes
    largeurs = []
    nb_colonnes = len(tableau[0])

    for j in range(nb_colonnes):
        maxi = 0
        for i in range(len(tableau)):
            if len(str(tableau[i][j])) > maxi:
                maxi = len(str(tableau[i][j]))
        largeurs.append(maxi + 3)

    # affichage final bien aligné
    for i in range(len(tableau)):
        ligne_affichee = ""
        for j in range(nb_colonnes):
            ligne_affichee += str(tableau[i][j]).ljust(largeurs[j])
        print(ligne_affichee)
