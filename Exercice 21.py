def somme_diviseurs(n):
    total = 1  # 1 est un diviseur de chaque nombre
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            total += i
            if i != n // i:  # Ajouter le quotient seulement s'il est différent du diviseur
                total += n // i
    return total

def trouver_nombres_amicaux(limite):
    somme_amicaux = 0
    for a in range(2, limite):
        b = somme_diviseurs(a)
        if a != b and somme_diviseurs(b) == a:
            somme_amicaux += a
    return somme_amicaux

limite = 10000
somme_amicaux = trouver_nombres_amicaux(limite)
print(somme_amicaux)
