def standardisation(af):
    #Créer un nouvel état 'I' 
    #Ajouter toutes les transitions des états iniiaux à 'I' qui est devenu l'état initial
    #Automate 6: anciens états initiaux 1 et 3 devenus inutiles(Aucun chemin ne mène à eux)
    nouvel_etat = 'I'
    af["etats"].insert(0, nouvel_etat)#Ajout de l'état I
    for tr in af['transitions']:
        if tr[0] == nouvel_etat:
            continue #Evite d'ajouter les mêmes transitions(car les transitions de I fera partie de la boucle)
        elif tr[0] in af['initial']:
            af['transitions'].append([nouvel_etat, tr[1], tr[2]])#ajout de la transition de I
    #print(af)
    af["initial"] = None
    af["initial"] = [nouvel_etat]
    #print(af)
    #supp_etat = []
    """for i in af['transitions']:
        supp_etat.append(i[0])
        supp_etat.append(i[2])
    for e in af['etats']:
        if e not in supp_etat:
            af['etats'].remove(e)"""
    return af


def est_standard(af):
    if len(af['initial']) > 1 or any(tr[2] in af['initial'] for tr in af['transitions']):
        print(af)
        print("Automate non standard")
        ans = input("Voulez-vous le standardisez? ecrivez OUI ou NON: ")
        if ans == "NON":
            return "Automate non standard"
        else:
            standardisation(af)
            print(af)
            return "Automate standardisée"
    else:
        return "Automate standard"
