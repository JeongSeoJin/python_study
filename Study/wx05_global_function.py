# global 변수의 값을 측정하여 판단하는 무언가.
# 1자리 숫자만 더해주는 계산기

import sys

print("="*26 + "\n Only digit!!![ 0 ~ 9 ]\n" + "="*26)

while True:
    global a
    a = input("First number : ")
    a = int(a)
    global b
    b = input("Second number : ")
    b = int(b)

    def mul():
        global a
        global b
        return a * b

    if a > 9:
        print("\nYou have wrong answer in fisrt\nYour answer : {}\n".format(a))
        continue

    if b > 9:
        print("You have wrong answer in second\nYour answer : {}\n".format(b))
        continue

    print(mul())

    re = input("Do you want to try again? [ yes | no ] : ")
    if re == "yes":
        continue
    elif re == "no":
        print("\nThanks for using this game :D\n")
        break
    else:
        print("Worng answer :(\nYour answer : {}\n".format(re))