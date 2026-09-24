
year = int(input("Year "))

if 1900 <= year <= 3000:
    if year % 4 == 0 and year % 100 != 0:
        print("Leap year.")
    elif year % 400 == 0: 
        print("Leap year.")
    else: 
        print("Ordinary year.")
else: 
    print("Try again")
    



