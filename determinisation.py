from affichage_automate import *

def est_deterministe(AF):
    test=True
    a = AF['alphabet']
    e = AF['etats']
    t = AF['transitions']
    count=0
    if est_epsilon(AF): #si il y a des epsilons, il n'est pas déterministe
        return test==False
    if len(AF['initial'])>1: #on vérifie qu'il n'y a pas plusieurs états initiaux
        test=False
        print("Il y a plusieurs états initiaux.")

    if test==True:
        for i in range (len(e)): #on vérifie que chaque état n'a pas plusieurs flèches d'un même symbole
            for j in range (len(a)):
                for k in range (len(t)):
                    if t[k][0]==e[i] and t[k][1]==a[j]: #on compare pour chaque transition
                        count+=1
                if count>1:
                    test=False
                    print("L'état",e[i],"a plusieurs flèches",a[j],)
                count=0

    if test==False:
        print("L'automate n'est pas déterministe.")
    else :
        print("L'automate est déterministe.")
    return test

def est_complet (AF):

    test = True
    a = AF['alphabet']
    e = AF['etats']
    t = AF['transitions']
    count = 0

    for i in range(len(e)):
        for j in range (len(a)) : #on vérifie que chaque état a une flèche pour chaque lettre de l'alphabet
            for k in range(len(t)):
                if t[k][0] == e[i] and t[k][1]==a[j] :
                    count += 1
            if count !=1:
                test = False
                print("L'état", e[i], "n'a pas une flèche pour chaque lettre.")

            count = 0

    if test == False:
        print("L'automate n'est pas complet.")
    else:
        print("L'automate est complet.")
    return test

def completion (AF):
    AF["etats"].append("P") #on crée l'état poubelle
    a = AF['alphabet']
    e = AF['etats']
    t = AF['transitions']
    check=False

    for i in range(len(e)): #si un état n'a pas de transition pour une lettre, on l'ajoute
        for j in range(len(a)):
            check=False
            for k in range(len(t)):
                if t[k][0]==e[i] and t[k][1]==a[j]:
                    check=True
            if check==False:
                t.append([e[i],a[j],"P"])


    return AF

def est_epsilon (AF):
    test = False
    e = AF['etats']
    t = AF['transitions']
    for i in range(len(e)): #on vérifie s'il y a des epsilons dans les transitions
        for j in range(len(t)):
            if t[j][1]=='ε' :
                test=True
    return test

def clotures (AF):
    e=AF['etats']
    t=AF['transitions']
    new_etats_af=[]
    clotures=[]

    for i in range (len(e)):
        new_etat=e[i]
        etat_trouve=[e[i]] #liste temporaire pour vérifier qu'on ne rate aucune transition ε des états suivants
        while len(etat_trouve)>0: #on regarde pour chaque etat s'il a d'autres transitions ε
            etat=etat_trouve.pop(0)
            for j in range(len(t)):
                if t[j][0]==etat and t[j][1]=='ε': #si il y a une transition ε on rajoute l'état à la liste etat_trouve
                    if t[j][2] not in new_etat.split("."):
                        new_etat = new_etat + "." + t[j][2]
                        etat_trouve.append(t[j][2])

        clotures.append(new_etat)
        new_etats_af.append(e[i]+"'")

    AF['etats']=new_etats_af
    AF['clotures']=clotures #on ajoute une clé clotures au dictionnaire pour avoir les correspondances avec les nouveaux états
    AF['initial']=[AF['etats'][0]]
    AF['final'] = [AF['etats'][len(AF['etats'])-1]]
    return AF

def trouve_cloture (AF,etat):
    cloture=""
    for i in range (len(AF['etats'])):
        if AF['etats'][i]==etat:
            cloture=AF['clotures'][i]
    return cloture

def determinisation_et_completion (AF):
    AFD={'etats':[],'alphabet':[],'initial':[],'final':[],'transitions':[]}
    AFD['alphabet']=AF['alphabet']
    initial=""
    epsilon=False
    final=AF['final']

    if est_epsilon(AF):
        epsilon=True
        AF = clotures(AF)
        AFD['clotures'] = AF['clotures']

    for i in range (len(AF['initial'])): #on ajoute l'état ou les états initiaux au nouvel automate
        if initial=="":
            initial=AF['initial'][i]
        else :
            initial=initial+"."+AF['initial'][i]

    AFD['initial'].append(initial)
    AFD['etats'].append(initial)

    e=AFD['etats']
    a=AFD['alphabet']
    t1=AF['transitions']
    t2=AFD['transitions']
    f=AFD['final']

    j=0

    while j<len(e): #déterminisation
        if epsilon :
            temp = e[j].split(".")
            etats = ""
            for z in range(len(temp)):
                if etats == "":
                    etats = trouve_cloture(AF, temp[z]) #on cherche les clotures pour avoir accès à toutes les transitions
                else:
                    etats = etats + "." + trouve_cloture(AF, temp[z])
        else:
            etats = e[j].split(".")

        for k in range (len(a)):
            fin=""
            for l in range (len(t1)):

                for w in range(len(etats)): #pour chaque etat de l'automate original présent dans l'etat, on regarde ses transitions
                    if t1[l][0]==etats[w] and t1[l][1]==a[k] : #on ajoute la transition si elle n'existe pas
                        if t1[l][2] not in fin:
                            if epsilon:
                                if fin == "":
                                    fin = t1[l][2] + "'"
                                else:
                                    fin = fin + "." + t1[l][2] + "'"
                            else:
                                if fin=="":
                                    fin=t1[l][2]
                                else :
                                    fin=fin+"."+t1[l][2]
            if fin!="":
                if fin not in e:
                    e.append(fin)
                t2.append([e[j],a[k],fin])
        j+=1

    if epsilon:

        for i in range (len(final)): #on indique quels états sont finaux
            for j in range(len(e)):
                check=False
                temp = e[j].split(".")
                etats = ""
                for z in range(len(temp)): #on regarde quels états finaux sont présents dans les clotures
                    if etats == "":
                        etats = trouve_cloture(AF, temp[z])
                    else:
                        etats = etats + "." + trouve_cloture(AF, temp[z])
                etats=etats.split(".")

                for k in range(len(etats)):
                    if etats[k] in final:
                        check=True
                if check and e[j] not in f:
                    f.append(e[j])

    else:

        for i in range (len(AF['final'])): #on indique quels états sont finaux
            for j in range(len(e)):
                check=False
                etats = e[j].split(".")

                for k in range(len(etats)):
                    if etats[k] in AF['final']:
                        check=True
                if check and e[j] not in f:
                    f.append(e[j])

    if est_complet(AFD)==False: #si l'automate n'est pas complet, on le complète
        AFDC=completion(AFD)
    else:
        AFDC=AFD
    return AFDC

def afficher_cloture (AFDC,AF):
    print()
    print("Table de correspondance pour les clôtures :")
    temp=[]
    for i in range(len(AFDC['etats'])):

        etats = AFDC['etats'][i].split(".")

        for j in range(len(etats)):
            if etats[j] not in temp:
                temp.append(etats[j])
                if etats[j]!="P":
                    cloture = trouve_cloture(AF, etats[j])
                    cloture=cloture.split(".")
                    print(etats[j], " <- {", end="")
                    for k in range(len(cloture)):
                        print(cloture[k], end="")
                        if k != len(cloture) - 1:
                            print(",", end="")


                    print("}")

def afficher_automate_deterministe_complet(AFDC):
    afficher_automate(AFDC)
    print()
    print("Table de correspondance :")
    for i in range (len(AFDC['etats'])): #pour chaque nouvel état, on indique à quels anciens états il correspond
        print(AFDC['etats'][i], end="")
        if AFDC['etats'][i]== "P":
            print( " <- poubelle")

        else :
            e = AFDC['etats'][i].split(".")
            print(" <- {", end="")
            for j in range (len(e)):
                print(e[j], end="")
                if j!=len(e)-1:
                    print(",", end="")
            print("} de l'automate original")

def test_determinisation_completion (AF):
    if est_deterministe(AF)==True:
        if est_complet(AF)==True:
            AFDC=AF
        else :
            AFDC=completion(AF)
    else :
        AFDC=determinisation_et_completion(AF)
    afficher_automate_deterministe_complet(AFDC)
    if "clotures" in AFDC: #si on a utilisé des clotures pour l'automate, on les affiche
        afficher_cloture(AFDC,AF)

    return AFDC



