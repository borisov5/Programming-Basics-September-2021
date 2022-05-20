flowers_type = input()
number_flowers = int(input())
budget = int(input())
flowers = 0

if flowers_type == "Roses":
    flowers = 5
elif flowers_type == "Dahlias":
    flowers = 3.8
elif flowers_type == "Tulips":
    flowers = 2.8
elif flowers_type == "Narcissus":
    flowers = 3
elif flowers_type == "Gladiolus":
    flowers = 2.5

if number_flowers > 80 and flowers_type == "Roses":
    flowers *= 0.9
elif number_flowers > 90 and flowers_type == "Dahlias":
    flowers *= 0.85
elif number_flowers > 80 and flowers_type == "Tulips":
    flowers *= 0.85
elif number_flowers < 120 and flowers_type == "Narcissus":
    flowers *= 1.15
elif number_flowers < 80 and flowers_type == "Gladiolus":
    flowers *= 1.20

total_cost = number_flowers * flowers
difference = abs(budget - total_cost)

if total_cost <= budget:
    print(f"Hey, you have a great garden with {number_flowers} {flowers_type} and {difference:.2f} leva left.")
else:
    print(f"Not enough money, you need {difference:.2f} leva more.")
