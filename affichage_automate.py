def afficher_automate(a):
    # affichage des informations principales de l'automate
    print("etats:", end=" ")
    for etat in a["etats"] :
        print(etat, end=" ")
    print()

    print("alphabet:", end=" ")
    for lettre in a["alphabet"] :
        print(lettre, end=" ")
    print()

    print("initial:", end=" ")
    for i in a["initial"] :
        print(i, end=" ")
    print()

    print("final:", end=" ")
    for f in a["final"] :
        print(f, end=" ")
    print()
    print()

    #création des noms de colonnes du tableau
    tableau = [[""]]
    tableau[0].append("Etat")
    for lettre in a["alphabet"]:
        tableau[0].append(lettre)

    #création des lignes du tableau
    for etat in a["etats"]:
        if etat in a["initial"] and etat in a["final"]:
            type_etat = "E/S"
        elif etat in a["initial"]:
            type_etat = "E"
        elif etat in a["final"]:
            type_etat = "S"
        else:
            type_etat = " "
        ligne = [type_etat, etat]

        for lettre in a["alphabet"]:
            ligne.append("")

        #remplissage des transitions
        i = 2
        arrivee = ""
        for lettre in a["alphabet"] :
            for t in a["transitions"] :
                if t[0] == ligne[1] and t[1] == lettre :
                    if ligne[i] == "" :
                        ligne[i] += t[2]
                    else:
                        ligne[i] += "," + t[2]
            i += 1

        for i in range(len(ligne)) :
            if ligne[i] == "" :
                ligne[i] += "--"

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
