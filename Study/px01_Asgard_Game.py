# Thor : Damage = 50, hp = 140
#     mjolnir : damage = 70
#     punch : damage = 20
#     thunder : damage = 50
# Hela : damage = 60, hp = 200
#     splinters : damage = 20 ~ 100

import sys

class ground():
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        print("="*20,"\nThis is {}".format(name))
        print("HP : {}".format(hp))
        print("="*20)

Asgard = ground("Asgard", 80000)

class unit():
    def __init__(self, name, hp, damage, weapon_check):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.weapon_check = weapon_check
        print("{} is in Asgard".format(name))
        print("Name : {0} | Hp : {1} | Damage : {2}".format(name, hp, damage))

    def weapon(self, name, damage):
        self.name = name
        self. damage = damage
        if self.weapon_check == "no":
            print("This Unit has not weapon")
        elif self.weapon_check == "yes":
            print("Weapon_Name : {0} | Damage : {1}". format(name, damage))
        
class enemy():
    def __init__(self, name, hp, damage, weapon_check):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.weapon_check = weapon_check
        print("Name : {0} | Hp : {1} | Damage : {2}".format(name, hp, damage))

    def weapon(self, name, damage):
        self.name = name
        self. damage = damage
        if self.weapon_check == "no":
            print("This Unit has not weapon")
        elif self.weapon_check == "yes":
            print("Weapon_Name : {0} | Damage : {1}". format(name, damage))
        

Thor = unit("Thor", 140, 50, "yes")
Thor.weapon("Mjolnir", 70)



print("\n")
print("="*30,"\nenemies are coming...")
print("="*30)

print("------Enemy informations------")
Hela = enemy("Hela", 200, 60, "yes")
Hela.weapon("splinters", "20 ~ 100")

print("\nIf you want to stop the game, write 'quit' whenever you want.")

class damaged_unit():
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
    def damaged(self, damaged):
        self. damaged = damaged
        print("{0} has damaged hp : {1} [-{2}]".format(self.name, self.hp, self.damaged))
class attack():
    def mjolnir(self, damage):
        self.damage = damage
        print("you attacked with Thor's Mjolnir.\n")

    def punch(self, damage):
        self.damage = damage
        print("You attacked with Thor's Powerful punch\n")
    def thunder(self, damage):
        self.damage = damage
        print("You attacked with Thor's Thunder\n")

while True:
    question = input("\nAre you ready to protect Asgrad from enemies?? [ yes | no ] : ")
    if question == "yes":
        print("Hela and Hela's army are coming to asgard.")
        enter = input("Click Enter Key : ")
        if enter == "":
            print("\nHela has arrived in Asgard.")
            break

        elif enter == "quit":
            print("[ you left the game ]")
            sys.exit()
        
    elif question == "no":
        print("you are not ready...")
    
    elif question == "quit":
        print("[ you left the game ]")
        sys.exit()
            

    else:
        print("="*35)
        print("You did write wrong answer.")
        print("Your answer : {}".format(question))
        print("="*35)
        

while True:
    question = input("\ndo you want to attack? [ yes | no ] : ")
    if question == "yes":
        question = input("Choose your skill [ mjolnir | punch | thunder ] : ")
        if question == "mjolnir":
            Mjolnir = attack()
            Mjolnir.mjolnir(70)
            Hela = damaged_unit("Hela", 130)
            Hela.damaged(70) #여기에 있는 hela의 hp 값을 변수로 지정해서 사용해야함. (일단 임시로 지정)
            
        elif question == "punch":
            Punch = attack()
            Punch.punch(20)
            Hela = damaged_unit("Hela", 180)
            Hela.damaged(20)
            
        elif question == "thunder":
            Thunder = attack()
            Thunder.thunder(50)
            Hela = damaged_unit("Hela", 150)
            Hela.damaged(50)
            
        elif question == "quit":
            print("[ you left the game ]")
            sys.exit()
        
        else:
            print("="*35)
            print("You did write wrong answer.")
            print("Your answer : {}".format(question))
            print("="*35)

    elif question == "no":
        print("you are no ready...")

    elif question == "quit":
        print("[ you left the game ]")
        sys.exit()

    else:
        print("="*35)
        print("You did write wrong answer.")
        print("Your answer : {}".format(question))
        print("="*35)
# except ValueError:
#     print("Wrong answer")
#     print("'ValueError'")

# except Exception as err:
#     print("Wrong answer")
#     print("Exception")

# except ZeroDivisionError as err:
#     print("Wrong answer")
#     print("ZeroDivisionError")

# except KeyboardInterrupt as err:
#     print("Wrong answer")
#     print("KeyboardInterrupt")
