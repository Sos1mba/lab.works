day = int(input("Day "))
days_in_month = [30, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

month = int(input("Month "))
month_order = [1,2,3,4,5,6,7,8,9,10,11,12]

year = int(input("Year "))

if day - 1 == 0:
    month_before = month - 2
else:
    month_before = month - 1

if day != 1:   
    day_before = day - 1
else:
    day_before = days_in_month[month_before]

if month == 1: 
    year_before = year - 1
else: 
    year_before = year


print(f"{day_before}.{month_order[month_before]}.{year_before}")
