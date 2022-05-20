budget = float(input())
category = input()
number_of_people = int(input())
price = 0

if category == "VIP":
    price = 499.99
elif category == "Normal":
    price = 249.99

if 1 <= number_of_people <= 4:
    budget *= 0.25
elif 5 <= number_of_people <= 9:
    budget *= 0.40
elif 10 <= number_of_people <= 24:
    budget *= 0.50
elif 25 <= number_of_people <= 49:
    budget *= 0.60
elif number_of_people > 49:
    budget *= 0.75

total_cost = number_of_people * price
difference = abs(total_cost - budget)

if budget >= total_cost:
      print(f"Yes! You have {difference:.2f} leva left.")
else:
    print(f"Not enough money! You need {difference:.2f} leva.")
