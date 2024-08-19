class cal():
    def multiply(self):
        try:
            print("Claculation But only multiply")
            a = input("Please write here first number you want. : ")
            b = input("Please write here second number you want. : ")
            print("\nFirst number is {}".format(a))
            print("Second number is {}".format(b))
            print("\ncalculated number : {}".format(int(a) + int(b)))

        except ValueError:
            print("ValueError...")
        except ZeroDivisionError as err:
            print("ZeroDivisionError...")
            print(err)

cal = cal()
cal.multiply()