encoded = input()

series = []
count = ""

for symbol in encoded:
    if symbol.isdigit():
        count += symbol
    else:
        length = int(count) if count else 1
        series.append(symbol * length)
        count = ""

print("".join(series))
