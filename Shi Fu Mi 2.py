import random
import curses
import pygame
import tkinter

def main(stdscr):

    curses.curs_set(0)  
    stdscr.clear()
    stdscr.refresh()


    symbols = ['pierre', 'papier', 'ciseaux']
    rules = {'pierre': 'ciseaux', 'ciseaux': 'papier', 'papier': 'pierre'}

    while True:
        stdscr.clear()
        stdscr.addstr(0, 0, "Bienvenue dans le jeu pierre-papier-ciseaux !")
        stdscr.addstr(2, 0, "Choisissez votre coup (pierre, papier, ciseaux) : ")
        stdscr.refresh()

       
        user_choice = stdscr.getstr(3, 0, 20).decode().strip().lower()

        
        if user_choice not in symbols:
            stdscr.addstr(4, 0, "Choix invalide ! Veuillez choisir entre pierre, papier ou ciseaux.")
            stdscr.refresh()
            stdscr.getch()  
            continue

        
        computer_choice = random.choice(symbols)

        stdscr.addstr(5, 0, f"Vous avez choisi : {user_choice}")
        stdscr.addstr(6, 0, f"L'ordinateur a choisi : {computer_choice}")
        stdscr.refresh()

        if user_choice == computer_choice:
            result = "Égalité !"
        elif rules[user_choice] == computer_choice:
            result = "Vous avez gagné !"
        else:
            result = "L'ordinateur a gagné !"

        stdscr.addstr(8, 0, result)
        stdscr.addstr(10, 0, "Appuyez sur une touche pour rejouer, ou 'q' pour quitter.")
        stdscr.refresh()

        key = stdscr.getch()

        if key == ord('q'):
            break

if __name__ == "__main__":
    curses.wrapper(main)