import sys 
try:
    n1 = int(input("Enter first number: "))
    n2 = int(input("Enter second number: "))
   
    result = 1
   
    while True:
        result += 10 ** n2
        if len(str(result)) > n2:
            result -= (10 ** (n1 - 1))
            result -= 1
            print(result)
            break  
except ValueError:
        print("Wrong value")