from determinisation import *

def automate_complementaire(A):
    new_final=[]
    for i in range (len(A['etats'])): #on inverse les états finaux (si pas final, l'état devient final et inversement)
        if A['etats'][i] not in A['final']:
            new_final.append(A['etats'][i])
    A['final']=new_final
    return A


