import sys
import math

def faire_200p():
    pieces = [1, 2, 5, 10, 20, 50, 100, 200]
    maniere = [0] * 201
    maniere[0] = 1


    for pence in pieces:
        for montant in range(pence, 201):
            maniere[montant] += maniere[montant - pence]
    return maniere[200]
resultat = faire_200p()
print(resultat)
