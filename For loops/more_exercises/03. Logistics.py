number_of_cargos = int(input())
price = 0
total_tons = 0
cargo_price = 0
total_price = 0
p1 = 0
p2 = 0
p3 = 0
for i in range(number_of_cargos):
    tons = int(input())
    total_tons = total_tons + tons
    if tons <= 3:
        price = 200
        cargo_price = tons * price
        p1 += tons
    elif 3 < tons <= 11:
        price = 175
        cargo_price = tons * price
        p2 += tons
    elif 12 <= tons:
        price = 120
        cargo_price = tons * price
        p3 += tons
    total_price += cargo_price
average_price = total_price  / total_tons
p1 = p1 / total_tons * 100
p2 = p2 / total_tons * 100
p3 = p3 / total_tons * 100
print(f"{average_price:.2f}")
print(f"{p1:.2f}%")
print(f"{p2:.2f}%")
print(f"{p3:.2f}%")