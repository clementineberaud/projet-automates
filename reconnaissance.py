def reconnaitre_mot(mot, A) :
    etat_actuel = A["initial"][0]
    t = A["transitions"]

    for lettre in mot :
        trouve = False

        if lettre not in A["alphabet"] :
            return "non"

        for transition in t :
            if lettre == transition[1] and etat_actuel == transition[0] :
                etat_actuel = transition[2]
                trouve = True
                break

        if not trouve :
            return "non"

    if etat_actuel in A["final"] :
        return "oui"
    else :
        return "non"