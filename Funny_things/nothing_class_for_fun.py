from warnings import catch_warnings
from pygame.constants import PREALLOC
from random import *

print("Hello world\n")

password_value = [] 

class person():
    global password_value

    def __init__(self):
        pass
    def change_password(self):

        list = [1,2,3,4,5,6,7,8,9,0]
        i = 0

        while i < 6:
            passwd = choice(list)
            password_value.append(passwd)
            # password_value.replace(",", "")
            i += 1

    def password(self, nm):
        self.change_password()
        
        if nm == "jeongseojin":
            a = password_value
            # print(self.change_password())
            print("Ok master, you got the password for key\n[Password : {}]".format(a))

        else:
            print("******** unidentified ********")

# key = person()
# key.password(input("Enter your name : "), 29130)

# pwd = person()
# pwd.change_password()

if  __name__ == "__main__":
    get_key = person()
    get_key.password(input("Enter your name : "))
