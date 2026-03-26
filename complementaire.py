from determinisation import *

def automate_complementaire(A):
    A=test_determinisation_completion(A)
    new_final=[]
    for i in range (len(A['etats'])):
        if A['etats'][i] not in A['final']:
            new_final.append(A['etats'][i])
    A['final']=new_final
    return A


