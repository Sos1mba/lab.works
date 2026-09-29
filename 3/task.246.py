n = int(input(""))

a = 1
b = 2

for i in range(1, n):
    a *= b 
    b += 1
    print(a,b)
    
print(a)
    