def afficher_automate(a):
    # affichage des informations principales
    print("Alphabet :", a["alphabet"])
    print("Etats :", a["etats"])
    print("Initial :", a["initial"])
    print("Final :", a["final"])
    print()

    # affichage de l'entête du tableau
    ligne = "    "
    for lettre in a["alphabet"]:
        ligne += lettre + "    "
    print(ligne)

    # parcours des états
    for etat in a["etats"]:
        debut = ""

        # on marque les états initiaux et/ou finaux
        if etat in a["initial"] and etat in a["final"]:
            debut = "E/S "
        elif etat in a["initial"]:
            debut = "E   "
        elif etat in a["final"]:
            debut = "S   "
        else:
            debut = "    "

        ligne = debut + str(etat) + "   "

        # affichage des transitions pour chaque lettre
        for lettre in a["alphabet"]:
            if etat in a["transitions"] and lettre in a["transitions"][etat]:
                dest = a["transitions"][etat][lettre]

                # si aucune transition
                if dest == []:
                    ligne += "--  "
                else:
                    # on construit le texte des destinations
                    texte = ""
                    for d in dest:
                        texte += str(d) + ","
                    texte = texte[:-1]  # enlever la dernière virgule
                    ligne += texte + "   "
            else:
                ligne += "--  "

        print(ligne)
