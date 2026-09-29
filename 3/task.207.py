import sys

while True:
    try:
        number = int(input(""))
        quantity = int(input(""))

        a = ""

        for i in range(quantity):
            a += f"{number} "
            
        print(a)
    except ValueError:
        print("Try again")