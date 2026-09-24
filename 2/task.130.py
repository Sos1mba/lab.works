program = 2700

amountOfPrograms = int(input("number of copies purchased "))

if amountOfPrograms < 10:
    print(f"The amount of discount is 0%, total amount of the purchase after the discount is UAH {program * amountOfPrograms}")
elif amountOfPrograms >= 10 and amountOfPrograms <= 19:
    total = program * amountOfPrograms
    print(f"The amount of discount is 10%, total amount of the purchase after the discount is UAH {total - total * 10 / 100}")
elif amountOfPrograms >= 20 and amountOfPrograms <= 49:
    total = program * amountOfPrograms
    print(f"The amount of discount is 20%, total amount of the purchase after the discount is UAH {total - total * 20 / 100}")
elif amountOfPrograms >= 50 and amountOfPrograms <= 99:
    total = program * amountOfPrograms
    print(f"The amount of discount is 30%, total amount of the purchase after the discount is UAH {total - total * 30 / 100}")
elif amountOfPrograms >= 100:
    total = program * amountOfPrograms
    print(f"The amount of discount is 40%, total amount of the purchase after the discount is UAH {total - total * 40 / 100}")