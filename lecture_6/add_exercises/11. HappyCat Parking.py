days = int(input())
hours = int(input())
price = 0
sum = 0
total_sum = 0
for x in range(1, days + 1):
    for y in range(1, hours + 1):
        if x % 2 == 0 and y % 2 == 1:
            price = 2.50
        elif x % 2 == 1 and y % 2 == 0:
            price = 1.25
        else:
            price = 1
        sum += price
    print(f"Day: {x} - {sum:.2f} leva")
    total_sum += sum
    sum = 0

print(f"Total: {total_sum:.2f} leva")