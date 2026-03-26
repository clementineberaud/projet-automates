def afficher_automate(a):
    print("Alphabet :", a["alphabet"])
    print("Etats :", a["etats"])
    print("Initiaux :", a["initiaux"])
    print("Finaux :", a["finaux"])
    print()

    ligne = "    "
    for lettre in a["alphabet"]:
        ligne += lettre + "    "
    print(ligne)

    for etat in a["etats"]:
        debut = ""

        if etat in a["initiaux"] and etat in a["finaux"]:
            debut = "E/S "
        elif etat in a["initiaux"]:
            debut = "E   "
        elif etat in a["finaux"]:
            debut = "S   "
        else:
            debut = "    "

        ligne = debut + str(etat) + "   "

        for lettre in a["alphabet"]:
            if etat in a["transitions"] and lettre in a["transitions"][etat]:
                dest = a["transitions"][etat][lettre]

                if dest == []:
                    ligne += "--  "
                else:
                    texte = ""
                    for d in dest:
                        texte += str(d) + ","
                    texte = texte[:-1]
                    ligne += texte + "   "
            else:
                ligne += "--  "

        print(ligne)

  def afficher_correspondance(cor):
    print()
    print("Correspondance :")

    for k in cor:
        print(str(k) + " -> " + str(cor[k]))
