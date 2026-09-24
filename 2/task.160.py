n = int(input(""))



if 1 < n < 9999:
    a = n // 100
    b = n % 100
        
    if b == 0:
        print(f"{a:.0f}")
    else:
        print(f"{a:.0f} {b:.0f}")
else: 
    print("type correct value")