import math
number_of_people = int(input())
entrance_tax = float(input())
sunbed_price = float(input())
umbrella_price = float(input())

entrance_taxes = number_of_people * entrance_tax
sunbed_taxes = math.ceil(number_of_people * 0.75) * sunbed_price
umbrella_taxes = math.ceil(number_of_people * 0.5) * umbrella_price

total_cost = entrance_taxes + sunbed_taxes + umbrella_taxes

print(f"{total_cost:.2f} lv.")