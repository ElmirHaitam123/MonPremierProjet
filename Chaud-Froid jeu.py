import random
import tkinter as tk

def jouer():
    global nombre_a_deviner, label_resultat
    nombre_a_deviner = random.randint(1, 1000)
    label_resultat.config(text="Le jeu a commencé! Devinez le nombre entre 1 et 1000.")

def verifier_proposition():
    try:
        proposition = int(proposition_entry.get())
        if proposition < 1 or proposition > 1000:
            label_resultat.config(text="Erreur: Veuillez entrer un nombre entre 1 et 1000.")
            return

        difference = abs(nombre_a_deviner - proposition)
        
        if difference == 0:
            label_resultat.config(text="Bien Joué! Vous avez deviné le nombre.")
        elif difference <= 25:
            label_resultat.config(text="Bouillant!")
        elif difference <= 50:
            label_resultat.config(text="Très chaud!")
        elif difference <= 100:
            label_resultat.config(text="Chaud!")
        elif difference <= 200:
            label_resultat.config(text="Assez chaud.")
        elif difference <= 300:
            label_resultat.config(text="Froid.")
        elif difference <= 400:
            label_resultat.config(text="Très froid.")
        elif difference <= 500:
            label_resultat.config(text="Glacé.")
        else:
            label_resultat.config(text="C'est Trop.")
    except ValueError:
        label_resultat.config(text="Erreur: Veuillez entrer un nombre valide.")

root = tk.Tk()
root.title("Jeu Chaud-Froid")
root.geometry("1280x720")

background_color = "Black"  
button_color = "Orange"  
text_color = "White"  

root.configure(bg=background_color)

label_titre = tk.Label(root, text="Bienvenue dans le jeu du Chaud-Froid !", bg=background_color, fg=text_color, font=("Helvetica", 32, "bold"))
label_titre.pack(pady=20)

label_instruction = tk.Label(root, text="Entrez votre proposition (entre 1 et 1000):", bg=background_color, fg=text_color, font=("Helvetica", 28))
label_instruction.pack(pady=20)

proposition_entry = tk.Entry(root, font=("Helvetica", 28), bg="Grey", fg=text_color)
proposition_entry.pack(pady=20)

btn_verifier = tk.Button(root, text="Vérifier", width=16, height=2, bg=button_color, fg="white", font=("Helvetica", 28, "bold"), command=verifier_proposition)
btn_verifier.pack(pady=20)

label_resultat = tk.Label(root, text="", bg=background_color, fg=text_color, font=("Helvetica", 28))
label_resultat.pack(pady=40)

btn_nouveau_jeu = tk.Button(root, text="Nouveau Jeu", width=16, height=2, bg=button_color, fg="white", font=("Helvetica", 28, "bold"), command=jouer)
btn_nouveau_jeu.pack(pady=20)

btn_quitter = tk.Button(root, text="Quitter", width=16, height=2, bg=button_color, fg="white", font=("Helvetica", 28, "bold"), command=root.quit)
btn_quitter.pack(pady=20)

jouer()

root.mainloop()
