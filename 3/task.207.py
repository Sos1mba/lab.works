import sys

while True:
    try:
        number = int(input(""))
        quantity = int(input(""))

        a = ""

        for i in range(quantity):
            a += f"{number} "
            
        print(a)
    except number < 0:
        print("Try again")