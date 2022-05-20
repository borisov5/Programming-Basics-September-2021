product = str(input().lower())
town = input().lower()
quantity = float(input())
if town == "sofia":
    if product == "coffee":
        print(0.50 * quantity)
    if product == "water":
        print(0.80 * quantity)
    if product == "beer":
        print(1.20 * quantity)
    if product == "sweets":
        print(1.45 * quantity)
    if product == "peanuts":
        print(1.60 * quantity)
if town == "varna":
    if product == "coffee":
        print(0.45 * quantity)
    if product == "water":
        print(0.70 * quantity)
    if product == "beer":
        print(1.10 * quantity)
    if product == "sweets":
        print(1.35 * quantity)
    if product == "peanuts":
        print(1.55 * quantity)
if town == "plovdiv":
    if product == "coffee":
        print(0.40 * quantity)
    if product == "water":
        print(0.70 * quantity)
    if product == "beer":
        print(1.15 * quantity)
    if product == "sweets":
        print(1.30 * quantity)
    if product == "peanuts":
        print(1.50 * quantity)
