rent = int(input())
statue = rent * 0.7
catering = statue * 0.85
sound = catering * 0.5
total_costs = rent + statue + catering + sound
print(f"{total_costs:.2f}")