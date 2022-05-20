budget = float(input())
number_of_nights = int(input())
price_per_night = float(input())
percent_additional_expenses = int(input())

if number_of_nights > 7:
    price_per_night *= 0.95

nights_total_price = price_per_night * number_of_nights
additional_expenses = budget * percent_additional_expenses / 100
total_sum = nights_total_price + additional_expenses
difference = abs(total_sum - budget)

if total_sum <= budget:
    print(f"Ivanovi will be left with {difference:.2f} leva after vacation.")
else:
    print(f"{difference:.2f} leva needed.")