import tkinter as tk
import random

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
    label_resultat.config(text=f"Vous avez choisi : {utilisateur}\nL'ordinateur a choisi : {ordinateur}\n{resultat}")

root = tk.Tk()
root.title("Jeu pierre-papier-ciseaux")
root.geometry("1000x800")

background_color = "#d5f4e6"
button_color = "#80ced6"
text_color = "#618685"

root.configure(bg=background_color)

label_titre = tk.Label(root, text="Bienvenue dans le jeu pierre-papier-ciseaux !", bg=background_color, fg=text_color, font=("Helvetica", 32, "bold"))
label_titre.pack(pady=40)

label_resultat = tk.Label(root, text="", bg=background_color, fg=text_color, font=("Helvetica", 28))
label_resultat.pack(pady=40)

frame_boutons = tk.Frame(root, bg=background_color)
frame_boutons.pack(pady=40)

btn_pierre = tk.Button(frame_boutons, text="Pierre", width=16, height=4, bg=button_color, fg="white", font=("Helvetica", 28, "bold"), command=lambda: jouer("pierre"))
btn_pierre.grid(row=0, column=0, padx=20, pady=10)

btn_papier = tk.Button(frame_boutons, text="Papier", width=16, height=4, bg=button_color, fg="white", font=("Helvetica", 28, "bold"), command=lambda: jouer("papier"))
btn_papier.grid(row=0, column=1, padx=20, pady=10)

btn_ciseaux = tk.Button(frame_boutons, text="Ciseaux", width=16, height=4, bg=button_color, fg="white", font=("Helvetica", 28, "bold"), command=lambda: jouer("ciseaux"))
btn_ciseaux.grid(row=0, column=2, padx=20, pady=10)

btn_quitter = tk.Button(root, text="Quitter", width=16, height=4, bg=button_color, fg="white", font=("Helvetica", 28, "bold"), command=root.quit)
btn_quitter.pack(pady=40)

root.mainloop()
