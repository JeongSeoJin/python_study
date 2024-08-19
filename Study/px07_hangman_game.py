from random import *
import sys

words = ["lemon", "apple", "grapefruits"]
topic = ""

print("This is a Hang Man Game!")
level = input("Choose level [1 ~ 5]\n : ")

if level == 1:
    print("Level : {}".format(level))
    topic = "words"


word_choiced = choice(topic)
print("\n=== The answer is {} ===\n".format(word_choiced))
letters = ""

while True:
    complete = True
    for w in word_choiced:
        if w in letters:
            print(w, end= " ")
        else:
            print("_", end= " ")
            complete = False
    print()

    if complete == True:
        print("**** Congraturation ****")
        break
    letter = input("Input >> ")
    if letter not in letters:
        letters += letter

    if letter in word_choiced:
        print("Correct!")
    else:
        print("Wrong")