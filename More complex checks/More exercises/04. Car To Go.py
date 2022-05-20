total_budget = float(input())
season = input()
budget = 0
car_class = ''
car = ''
if total_budget <= 100:
    if season == "Summer":
        budget = total_budget * 0.35
        car = "Cabrio"
        car_class = "Economy class"
    elif season == "Winter":
        budget = total_budget * 0.65
        car = "Jeep"
        car_class = "Economy class"
elif 100 < total_budget <= 500:
    if season == "Summer":
        budget = total_budget * 0.45
        car = "Cabrio"
        car_class = "Compact class"
    elif season == "Winter":
        budget = total_budget * 0.80
        car = "Jeep"
        car_class = "Compact class"
elif total_budget > 500:
    if season == "Summer":
        budget = total_budget * 0.90
        car = "Jeep"
        car_class = "Luxury class"
    elif season == "Winter":
        budget = total_budget * 0.90
        car = "Jeep"
        car_class = "Luxury class"

print(car_class)
print(f"{car} - {budget:.2f}")
