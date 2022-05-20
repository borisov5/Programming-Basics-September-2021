money = float(input())
year = int(input())
age = 17
spend_money = 0
for i in range(1800, year + 1):
    if i % 2 == 0:
        money -= 12000
    elif i % 2 == 1:
        age += 2
        spend_money = (age * 50)
        money -= (12000 + spend_money)
if money >= 0:
    print(f"Yes! He will live a carefree life and will have {money:.2f} dollars left.")
else:
    difference = abs(money)
    print(f"He will need {difference:.2f} dollars to survive." )
