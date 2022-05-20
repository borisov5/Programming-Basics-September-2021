import math
height = int(input())
width = int(input())
percent = int(input())
command = input()
area = height * width * 4
area_without_doors_and_windows = area * ((100 - percent) / 100)
area_left = math.ceil(area_without_doors_and_windows)

while command != "Tired!":
    litters = int(command)
    area_left -= litters
    if area_left <= 1:
        break
    command = input()

if command == "Tired!":
    print(f"{area_left} quadratic m left.")
elif area_left < 0:
    print(f"All walls are painted and you have {abs(area_left)} l paint left!")
else:
    print("All walls are painted! Great job, Pesho!")