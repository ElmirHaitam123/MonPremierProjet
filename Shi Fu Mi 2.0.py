import tkinter as tk
import random

# Fonctions pour le jeu de pierre-papier-ciseaux
def choix_ordi():
    return random.choice(['pierre', 'papier', 'ciseaux'])

def determiner_gagnant(choix_utilisateur, choix_ordi):
    if choix_utilisateur == choix_ordi:
        return "Égalité !"
    elif (choix_utilisateur == 'pierre' and choix_ordi == 'ciseaux') or \
         (choix_utilisateur == 'ciseaux' and choix_ordi == 'papier') or \
         (choix_utilisateur == 'papier' and choix_ordi == 'pierre'):
        return "Vous avez gagné !"
    else:
        return "L'ordinateur a gagné !"

def jouer(choix):
    utilisateur = choix
    ordinateur = choix_ordi()
    resultat = determiner_gagnant(utilisateur, ordinateur)
    
    # Mettre à jour l'interface graphique avec le résultat
    label_resultat.config(text=f"Vous avez choisi : {utilisateur}\nL'ordinateur a choisi : {ordinateur}\n{resultat}")

# Création de l'interface graphique avec Tkinter
root = tk.Tk()
root.title("Jeu pierre-papier-ciseaux")

# Titre
label_titre = tk.Label(root, text="Bienvenue dans le jeu pierre-papier-ciseaux !")
label_titre.pack(pady=10)

# Zone de résultat
label_resultat = tk.Label(root, text="")
label_resultat.pack(pady=20)

# Boutons pour les choix de l'utilisateur
frame_boutons = tk.Frame(root)
frame_boutons.pack()

btn_pierre = tk.Button(frame_boutons, text="Pierre", width=10, command=lambda: jouer("pierre"))
btn_pierre.grid(row=0, column=0, padx=10, pady=5)

btn_papier = tk.Button(frame_boutons, text="Papier", width=10, command=lambda: jouer("papier"))
btn_papier.grid(row=0, column=1, padx=10, pady=5)

btn_ciseaux = tk.Button(frame_boutons, text="Ciseaux", width=10, command=lambda: jouer("ciseaux"))
btn_ciseaux.grid(row=0, column=2, padx=10, pady=5)

# Bouton pour quitter
btn_quitter = tk.Button(root, text="Quitter", command=root.quit)
btn_quitter.pack(pady=10)

# Lancer l'interface graphique
root.mainloop()