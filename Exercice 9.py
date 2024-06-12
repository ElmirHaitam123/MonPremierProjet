def Theo_pythagore(somme):
    for a in range(1, somme// 3):
        for b in range(1, somme// 2):
            c = somme - a -b
            if a**2 + b**2 == c**2:
                return a,b,c
    return None 
Theoreme = Theo_pythagore(1000)
if Theoreme:
    a,b,c = Theoreme 
    produit = a*b*c
    print(f"Le Théorème de Pythagore est : {a,b,c}")
    print(f"Le produit abc est : {produit}")