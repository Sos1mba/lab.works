sum_n = 0
square_sum = 0

while True:
    n = int(input(""))
    sum_n += n
    square_sum += n * n 
    if sum_n == 0:
        break
print(square_sum)