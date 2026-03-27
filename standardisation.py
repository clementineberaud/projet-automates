def standardisation(af):
    """Problème à l'automate 3: anciens états initiaux devenus inutiles"""
    nouvel_etat = 'I'
    af["etats"].insert(0, nouvel_etat)
    for tr in af['transitions']:
        if tr[0] == nouvel_etat:
            continue
        elif tr[0] in af['initial']:
            af['transitions'].append([nouvel_etat, tr[1], tr[2]])
    #print(af)
    af["initial"] = None
    af["initial"] = [nouvel_etat]
    #print(af)
    supp_etat = []
    for i in af['transitions']:
        supp_etat.append(i[0])
        supp_etat.append(i[2])
    for e in af['etats']:
        if e not in supp_etat:
            af['etats'].remove(e)
    return af

"""def est_standard(af):
    if len(af['initial']) > 1:
        print("Automate non standard")
        a = int(input("Mettez un 1 pour standardiser, 0 sinon: "))
    for tr in af['transitions']:
        if tr[2] == af['initial'][0]:
            print("Automate non standard")
            a = int(input("Mettez un 1 pour standardiser, 0 sinon: "))
            break
        if a == 0:
            return "Automate non standard"
        elif a == 1:
            af = standardisation(af)
            print("Automate standardise!")
            return af"""

def est_standard(af):
    if len(af['initial']) > 1 or any(tr[2] in af['initial'] for tr in af['transitions']):
        print("Automate non standard")
        ans = input("Voulez-vous le standardisez? ecrivez OUI ou NON: ")
        if ans == "NON":
            return "Automate non standard"
        else:
            standardisation(af)
            return "Automate standardisée"
    else:
        return "Automate standard"
