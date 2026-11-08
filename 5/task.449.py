numbers = list(map(int, input().split()))

unique = []
for number in numbers:
    if numbers.count(number) == 1:
        unique.append(number)

print(*unique)
