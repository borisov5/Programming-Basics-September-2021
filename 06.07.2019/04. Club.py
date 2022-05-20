price_of_cocktail = 0
total_price = 0
profit = 0
desired_profit = float(input())
cocktail = input()
number_of_cocktails = int(input())
while True:
    price_of_cocktail = len(cocktail)
    total_price = 0
    total_price += (price_of_cocktail * number_of_cocktails)
    if total_price % 2 == 1:
        total_price *= 0.75
    profit += total_price
    if profit >= desired_profit:
        break
    cocktail = input()
    if cocktail == "Party!":
        break
    number_of_cocktails = int(input())

if profit >= desired_profit:
    print("Target acquired.")
else:
    difference = abs(desired_profit - profit)
    print(f"We need {difference:.2f} leva more.")
print(f"Club income - {profit:.2f} leva.")