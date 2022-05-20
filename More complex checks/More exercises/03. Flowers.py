chrysanthemum = int(input())
roses = int(input())
tulips = int(input())
season = input()
holiday = input()

chrysanthemum_price = 0
roses_price = 0
tulips_price = 0
total_price = 0

if season == "Spring" or season == "Summer":
    chrysanthemum_price = 2
    roses_price = 4.10
    tulips_price = 2.50
elif season == "Autumn" or season == "Winter":
    chrysanthemum_price = 3.75
    roses_price = 4.50
    tulips_price = 4.15

if holiday == "Y":
    chrysanthemum_price *= 1.15
    roses_price *= 1.15
    tulips_price *= 1.15

total_price = chrysanthemum * chrysanthemum_price + roses * roses_price + tulips * tulips_price
sum_flowers = chrysanthemum + roses + tulips
if tulips > 7 and season == "Spring":
    total_price *= 0.95
if roses >= 10 and season == "Winter":
    total_price *= 0.90
if sum_flowers > 20:
    total_price *= 0.80

total_price += 2

print(f"{total_price:.2f}")
