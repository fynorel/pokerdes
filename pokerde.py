#! /usr/bin/env python3
#! encoding:'utf-8'

import random
from itertools import groupby

neuf = 1
dix = 2
valet = 3
reine = 4
roi = 5
ass = 6

noms = {neuf: "9", dix: "10", valet: "J", reine: "Q", roi: "K", ass: "A"}

score_joueur = 0
score_ordi = 0

def start():
    print("Jouons au jeu de Poker aux dés.")
    while game():
        pass
    scores()

def game():
    print("L'ordinateur va vous aider à lancer vos dés.")
    throws()
    return play_again()

def throws(): 
    roll_number = 5
    dice = roll(roll_number)
    dice.sort()
    for i in range(len(dice)):
        print("Dés", i + 1, ":", noms[dice[i]])
    resultat = hand(dice)
    print("Vous avez actuellement :", resultat)
    while True:
        rerolls = int(input("Combien de dés souhaitez-vous relancer ? "))
        try:
            if rerolls in (0, 1, 2, 3, 4, 5):
                break
        except ValueError:
            pass
        print("Je n'ai pas compris. Veuillez saisir 0, 1, 2, 3, 4 ou 5.")

        if rerolls == 0:
            print("Vous terminez avec :", resultat)
        else:
            roll_number = rerolls
            dice_rerolls = roll(roll_number)
            dice_changes = list(range(rerolls))
            print("Saisissez le numéro du dés à rejouer : ")
            iterations = 0
            while iterations < rerolls:
                iterations = iterations + 1
                while True:
                    selection = int(input("?"))
                    try:
                        if selection in (1, 2, 3, 4, 5):
                            break
                    except ValueError:
                        pass
                    print("Je n'ai pas compris. Veuillez saisir 1, 2, 3, 4 ou 5.")
                dice_changes[iterations - 1] = selection -1
                print("Vous avez changé de dés", selection)
            iterations = 0
            while iterations < rerolls:
                iterations += 1
                replacement = dice_rerolls[iterations - 1]
                dice[dice_changes[iterations - 1]] = replacement
            dice.sort()
            for i in range(len(dice)):
                print("Dé", i + 1, ":", noms[dice[i]])
            resultat = hand(dice)
            print("Vous terminez avec", resultat)

def roll(roll_number):
    numbers = range(1, 7)
    dice = list(range(roll_number))
    iterations = 0
    #print(dice)
    while iterations < roll_number:
        iterations += 1
        #print(dice)
        dice[iterations-1] = random.choice(numbers)
    return dice

def hand(dice):
    dice_hand = [len(list(group)) for keys, group in groupby(dice)]
    dice_hand.sort(reverse = True)
    straight1 = [1, 2, 3, 4, 5]
    straight2 = [2, 3, 4, 5, 6]

    if dice == straight1 or dice == straight2:
        return "Une suite !"
    elif dice_hand[0] == 5:
        return "Cinq cartes identiques !"
    elif dice_hand[0] == 4:
        return "Poker !"
    elif dice_hand[0] == 3:
        if dice_hand[1] == 2:
            return "Full !"
        else:
            return "Brelan !"
    elif dice_hand[0] == 2:
        if dice_hand[1] == 2:
            return "Deux paires !"
        else:
            return "Une paire !"
    else:
        return "Une carte haute !"

def play_again():
    reponse = input("Voulez-vous rejouer ? o/n : ")
    if reponse in ("o", "O"):
        return reponse
    else:
        print("Merci d'avoir joué. A bientôt")
        return

def scores():
    global score_joueur, score_ordi
    print("MEILLEURS SCORES")
    print("Joueur : ", score_joueur)
    print("Ordinateur : ", score_ordi)

if __name__ == "__main__":
    start()





