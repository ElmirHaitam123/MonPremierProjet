from datetime import date

def compter_dimanches_premier_mois(annee_debut, annee_fin):
    compte_dimanches = 0
    
    # Boucle à travers chaque année et chaque mois
    for annee in range(annee_debut, annee_fin + 1):
        for mois in range(1, 13):
            if date(annee, mois, 1).weekday() == 6:  # 6 correspond à dimanche
                compte_dimanches += 1
                
    return compte_dimanches

annee_debut = 1901
annee_fin = 2000

compte_dimanches = compter_dimanches_premier_mois(annee_debut, annee_fin)
print(compte_dimanches)

