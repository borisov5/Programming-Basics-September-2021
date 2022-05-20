beverage = input()
sugar = input()
number_beverages = int(input())
price = 0
if beverage == "Espresso":
    if sugar == "Without":
        price = 0.90 * 0.65
    elif sugar == "Normal":
        price = 1
    elif sugar == "Extra":
        price = 1.20
elif beverage == "Cappuccino":
    if sugar == "Without":
        price = 1 * 0.65
    elif sugar == "Normal":
        price = 1.20
    elif sugar == "Extra":
        price = 1.60
elif beverage == "Tea":
    if sugar == "Without":
        price = 0.50 * 0.65
    elif sugar == "Normal":
        price = 0.60
    elif sugar == "Extra":
        price = 0.70

if beverage == "Espresso" and number_beverages >= 5:
    price *= 0.75
end_price = number_beverages * price
if end_price > 15:
    end_price *= 0.80
print(f"You bought {number_beverages} cups of {beverage} for {end_price:.2f} lv.")