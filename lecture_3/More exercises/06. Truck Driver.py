season = input()
kilometers_per_month = float(input())
sum = 0
if season == "Spring" or season == "Autumn":
    if kilometers_per_month <= 5000:
        sum = 0.75
    elif 5000 < kilometers_per_month <= 10000:
        sum = 0.95
    elif 10000 < kilometers_per_month <= 20000:
        sum = 1.45
elif season == "Summer":
    if kilometers_per_month <= 5000:
        sum = 0.90
    elif 5000 < kilometers_per_month <= 10000:
        sum = 1.10
    elif 10000 < kilometers_per_month <= 20000:
        sum = 1.45
elif season == "Winter":
    if kilometers_per_month <= 5000:
        sum = 1.05
    elif 5000 < kilometers_per_month <= 10000:
        sum = 1.25
    elif 10000 < kilometers_per_month <= 20000:
        sum = 1.45

salary = kilometers_per_month * sum * 4 * 0.90
print(f"{salary:.2f}")
