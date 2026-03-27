def standardisation(af):
    nouvel_etat = 'I'
    af_std = af.copy()
    af_std['etats'] = [nouvel_etat]#Ajout de l'état initial dans le nouvel automate
    af_std['initial'] = [nouvel_etat]#Ajout de l'état initial dans le nouvel automate
    af_std['transitions'] = []
    etat_afstd = []#etats utiles qu'on vas rajouter à la fin
    for tr in af['transitions']:
        if tr[0] == nouvel_etat:
            continue  # Evite d'ajouter les mêmes transitions(car les transitions de I fera partie de la boucle)
        elif tr[0] in af['initial']:
            af_std['transitions'].append([nouvel_etat, tr[1], tr[2]]) # ajout de la transition de I le nouvel état initial
            if tr[2] not in etat_afstd:
                etat_afstd.append(tr[2])
            if tr[0] == tr[2]:#si l'état reboucle sur lui même, on garde la transition
                af_std['transitions'].append(tr)
                if tr[2] not in etat_afstd:
                    etat_afstd.append(tr[2])
            if tr[0] in af['initial'] and tr[0] in af['final']:#si l'ancienne état initial est final, I doit être final aussi
                af_std['final'].append(nouvel_etat)
                af_std['transitions'].append(tr)#ajout de la transition de l'ancien état initial
                if tr[0] not in etat_afstd:
                    etat_afstd.append(tr[0])
        else:
            af_std['transitions'].append(tr)#ajout des transitions intermédiaires
            if tr[2] not in etat_afstd and tr[0] not in etat_afstd:
                etat_afstd.extend([tr[0], tr[2]])
        if tr[2] in af['initial'] and tr not in af['transitions']:
            af_std['transitions'].append(tr)
            """if tr[0] != tr[2]:
                transition_supp.append(tr)"""
    af_std['etats'] += sorted(etat_afstd)#ajout des etats utiles dans l'ordre croissant
    return af_std



def est_standard(af):
    if len(af['initial']) > 1 or any(tr[2] in af['initial'] for tr in af['transitions']):#conditions de la standardisation
        print("Automate non standard")
        ans = input("Voulez-vous le standardiser ? Écrivez OUI ou NON: ")
        if ans == "NON":
            return af
        else:
            print()
            print("Automate standardisé :")
            af_std = standardisation(af)
            return af_std
    else:
        return af

