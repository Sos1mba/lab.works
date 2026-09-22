base_seconds = int(input("Type in seconds : "))

seconds = base_seconds % 60

base_minutes = base_seconds // 60

minutes = base_minutes % 60

hours = base_minutes // 60             

while hours > 23:
    hours -= 24

print(f"{hours:02d}:{minutes:02d}:{seconds:02d}")
# print(f"hours {hours:02d}")
# print(f"min {minutes:02d}")
# print(f"sec {seconds:02d}")



# days = 0

# total_seconds = seconds % 60

# minutes = seconds // 60

# while seconds > 60:
#     minutes += 1
#     seconds -= 60

# while minutes >= 60:
#     if hours > 23:
#         hours -= 24
#         days += 1
#     else:
#         minutes -= 60
#         hours += 1
        
# print(minutes, total_seconds)



 