import sys

try:
    class robot():
        def __init__(self, input_name):
            self.input_name = input_name
            print("\nYour robot name : " + input_name)

        def head(self, part):
            self.part = part
            print("Head : {}".format(part))

        def arm(self, part):
            self.part = part
        
        def body(self, part):
            self.part = part
        
        def leg(self, part):
            self.part = part

    class end():
        def __init__(self):
            print()

        def quit(self):
            print("[You left the Game]")
            sys.exit()

    question = input("\nWrite your robot name : ")
    Robot = robot(question)
    Robot.head("Head Part")

    question1 = input("You want to left the game? [ yes | no ]")
    if question1 == "yes":
        qt = end()
        qt.quit()
    elif question1 == "no":
        pass

except KeyboardInterrupt as err:
    print("Wrong answer.")

finally:
    print("\nThanks for using this game!")
