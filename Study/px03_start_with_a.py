from random import *
from time import *
from px04_start_with_a_words import start_a, res
import sys

your_words = [""]

while True:
    print("="*39)
    print("  This game is the world hardest game")
    print("="*39)
    word_choice = input("chose a word you want to do [a ~ z]\n : ")
    if word_choice == "a":
        print("="*48 + "\n\n  If you want to surrender, enter 'surrender'")
        print("  Write here a word that start with 'a'")
        while True:
            print("="*20)
            your_turn = input(" : ")
            print("Your answer\n>> {}".format(your_turn))

            if your_turn in your_words:
                print("########caution########")
                print("  Same answer\n  Your answer : {}\n  Please write again".format(your_turn))
                print("#"*24)
                continue

            if your_turn == "surrender":
                print("="*22 + "\n Wasted...\n" + " Thanks for using :D\n" + "="*22)
                sys.exit()
                
            elif your_turn not in your_words:
                your_words.append(your_turn)

            if your_turn[0] != "a":
                print("########caution########")
                print("  Worng answer\n  Your answer : {}\n  Please write again".format(your_turn))
                print("#"*24)
                continue
            start_a()

            # if res.restart == "yes":
            #     continue
            # elif res.restart == "no":
            #     print("\n*** Thanks for using this game! :D ***\n\n")
            #     break
            # if len(start_a) == 0:
            #     print("="*12 + "\n You win!!\n" + "="*12)
            #     restart = input("Try again? [ yes | no ]\n : ")
            # if restart == "yes":
            #     sys.exit()
            # elif restart == "no":
            #     print(" ")
            #     print("="*22 + " Thanks for using this game!" + "="*22)
            #     sys.exit()