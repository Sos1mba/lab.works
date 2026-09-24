import math


r = int(input("radius: "))
n = int(input("Service selecter: "))

if n == 1: 
    print(f"Lenght = {2 * math.pi * r:.2f}")
elif n == 2:
    print(f"S = {math.pi * r ** 2:.2f}")
elif n == 3:
   print(f"V = {(4 / 3) * math.pi * r ** 3:.2f}")
elif n == 4:
    print(f"S = {4 * math.pi * r ** 2:.2f}")
