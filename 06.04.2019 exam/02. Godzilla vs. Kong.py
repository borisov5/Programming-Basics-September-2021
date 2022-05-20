film_budget = float(input())
sum_statists = int(input())
price_cloths = float(input())
import math
decor = film_budget * 0.10
if sum_statists > 150:
    price_cloths = price_cloths - price_cloths * 0.10
sum_cloths = sum_statists * price_cloths
film_budget = film_budget - sum_cloths - decor
if film_budget < 0:
    film_budget = abs(film_budget)
    print("Not enough money!")
    print(f"Wingard needs {film_budget:.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {film_budget:.2f} leva left.")