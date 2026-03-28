from affichage_automate import *

def standardisation(AF):
    initial = "I"
    AF['etats'].append(initial)
    for i in AF['initial']:
        for tr in AF['transitions']:
            if tr[0] == i:
                AF['transitions'].append(["I", tr[1], tr[2]])
            if tr[0] in AF['final']:
                if "I" not in AF['final']:
                    AF['final'].append("I")
    AF['initial'] = [initial]
    return AF

def est_standard(af):
    if len(af['initial']) > 1 or any(tr[2] in af['initial'] for tr in af['transitions']):#conditions de la standardisation
        print("Automate non standard")
        ans = input("Voulez-vous le standardiser ? Écrivez oui ou non : ")
        if ans == "non":
            return af
        else:
            print()
            print("Automate standardisé :")
            af_std = standardisation(af)
            afficher_automate(af_std)
            return af_std
    else:
        print("Automate standard")
        return af

