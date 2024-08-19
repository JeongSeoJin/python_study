import random
print("Let's figure out the number!")
opportunity = 7
answer = random.randrange(0, 101)

print("Opportunity : {}".format(opportunity))

try:
    while opportunity > 0:
        opportunity -= 1
        question = input(" : ")
        if int(question) > answer:
            print("Down")
            print("Opportunity : {}\n".format(opportunity))
        elif int(question) < answer:
            print("Up")
            print("Opportunity : {}\n".format(opportunity))
        if opportunity == 0:
            print("Wasted.....")
            print("The answer was {}".format(answer))
            
except ValueError:
    print("="*30)
    print("ValueError")
    print("="*30)
except ZeroDivisionError as err:
    print("="*30)
    print("ZeroDivisionError")
    print("="*30)
finally:
    print("Thanks for using this game :D")