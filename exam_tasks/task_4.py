number_days = int(input())
litters = 0
total_degrees = 0
for i in range(number_days):
    sum_rakia = float(input())
    degrees = float(input())
    litters += sum_rakia
    sum_degrees = sum_rakia * degrees
    total_degrees += sum_degrees

print(f"Liter: {litters:.2f}")
total_degrees /= litters
print(f"Degrees: {total_degrees:.2f}")

if total_degrees < 38:
    print("Not good, you should baking!")
elif 38 <= total_degrees <= 42:
    print("Super!")
elif total_degrees > 42:
    print("Dilution with distilled water!")