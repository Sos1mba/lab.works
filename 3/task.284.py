print("Type 0 to end cycle")
biggest = 0
biggest_n = 1
while True:
    n = int(input(""))
    if n == 0:
        break
    if n > biggest:
        biggest = n
    elif n == biggest:
        biggest_n += 1
    
print(biggest_n)