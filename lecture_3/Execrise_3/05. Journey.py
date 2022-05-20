budget = float(input())
season = input()
type_journey = ''
if budget <= 100:
    if season == "summer":
        budget *= 0.30
        destination = "Bulgaria"
        type_journey = "Camp"
    elif season == "winter":
        budget *= 0.70
        destination = "Bulgaria"
        type_journey = "Hotel"
elif 100 <= budget <= 1000:
    if season == "summer":
        budget *= 0.40
        destination = "Balkans"
        type_journey = "Camp"
    elif season == "winter":
        budget *= 0.80
        destination = "Balkans"
        type_journey = "Hotel"
elif budget > 1000:
    budget *= 0.90
    destination = "Europe"
    type_journey = "Hotel"

print(f"Somewhere in {destination}")
print(f"{type_journey} - {budget:.2f}")