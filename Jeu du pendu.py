import random
import tkinter as tk
from tkinter import messagebox

# Fonctions du jeu

def choisir_mot():
    mots = ["python", "ordinateur", "programmation", "jeu", "pendu"]
    return random.choice(mots)

def afficher_pendu(tentatives):
    etapes = [
        """
           -----
           |   |
               |
               |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
               |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        =========
        """
    ]
    label_pendu.config(text=etapes[tentatives])

def deviner():
    global tentatives, mot_cache, lettres_devinees

    lettre = entry_lettre.get().lower()
    entry_lettre.delete(0, tk.END)

    if lettre in lettres_devinees:
        messagebox.showinfo("Info", "Vous avez déjà deviné cette lettre.")
        return

    lettres_devinees.append(lettre)

    if lettre in mot:
        mot_cache = "".join([lettre if lettre == mot[i] else mot_cache[i] for i in range(len(mot))])
        label_mot.config(text=mot_cache)
    else:
        tentatives += 1
        afficher_pendu(tentatives)

    if "_" not in mot_cache:
        messagebox.showinfo("Félicitations", f"Bravo! Vous avez deviné le mot: {mot}")
        reset()
    elif tentatives >= 6:
        messagebox.showinfo("Perdu", f"Vous avez perdu! Le mot était: {mot}")
        reset()

def reset():
    global mot, mot_cache, tentatives, lettres_devinees
    mot = choisir_mot()
    mot_cache = "_" * len(mot)
    tentatives = 0
    lettres_devinees = []
    label_mot.config(text=mot_cache)
    afficher_pendu(tentatives)

# Configuration de l'interface graphique

root = tk.Tk()
root.title("Jeu du Pendu")
root.geometry("1280x720")

# Frame principale pour le jeu
frame_jeu = tk.Frame(root)
frame_jeu.pack(pady=20)

# Titre du jeu
label_titre = tk.Label(frame_jeu, text="Bienvenue au jeu du pendu!", font=("Helvetica", 24))
label_titre.pack()

# Affichage du pendu
label_pendu = tk.Label(frame_jeu, text="", font=("Courier", 18))
label_pendu.pack()

# Affichage du mot caché
label_mot = tk.Label(frame_jeu, text="", font=("Helvetica", 24))
label_mot.pack()

# Frame pour l'entrée de la lettre
frame_input = tk.Frame(frame_jeu)
frame_input.pack(pady=20)

# Label d'instruction
label_instruction = tk.Label(frame_input, text="Devinez une lettre:", font=("Helvetica", 18))
label_instruction.pack(side=tk.LEFT)

# Entrée pour la lettre
entry_lettre = tk.Entry(frame_input, font=("Helvetica", 18))
entry_lettre.pack(side=tk.LEFT)

# Bouton pour deviner
bouton_deviner = tk.Button(frame_input, text="Deviner", font=("Helvetica", 18), command=deviner)
bouton_deviner.pack(side=tk.LEFT, padx=20)

# Initialiser le jeu
reset()

# Lancement de la boucle principale
root.mainloop()

