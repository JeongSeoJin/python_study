import sys

def add():
    print("{0} + {1} = {2}".format(number1, number2, number1 + number2))

def sub():
    print("{0} - {1} = {2}".format(number1, number2, number1 - number2))

def mul():
    print("{0} * {1} = {2}".format(number1, number2, number1 * number2))

def div():
    print("{0} / {1} = {2}".format(number1, number2, number1 / number2))

print("="*48)
print("\tThis is Jeong Seo Jin calculator.")
print("="*48)
while True:
    equation = input("\nWrite here the Number Sentance that you want.\n[ add | sub | mul | div ] : ")

    print("Write here two numbers that you want to {0}\n".format(equation))
    number1 = input(" : ")
    number2 = input(" : ")
    number1 = int(number1)
    number2 = int(number2)

    if equation == "add":
        add()

    elif equation == "sub":
        sub()

    elif equation == "mul":
        mul()

    elif equation == "div":
        div()
    
    else:
        print("Wrong answer.. \nYour answer : {}".format(equation))

    ext = input("You want to leave this program?? [ yes | no ] : ")
    if ext == "yes":
        print("Thanks for using this program! :D")
        break
        sys.exit
    elif ext == "no":
        continue

    else:
        print("Wrong answer.. \nYour answer : {}".format(ext))
