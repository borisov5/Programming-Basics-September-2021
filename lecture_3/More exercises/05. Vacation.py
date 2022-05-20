budget = float(input())
season = input()
place = ''
location = ''

if budget <= 1000:
    place = "Camp"
    if season == "Summer":
        location = "Alaska"
        budget *= 0.65
    elif season == "Winter":
        location = "Morocco"
        budget *= 0.45
elif 1000 < budget <= 3000:
    place = "Hut"
    if season == "Summer":
        location = "Alaska"
        budget *= 0.80
    elif season == "Winter":
        location = "Morocco"
        budget *= 0.60
elif budget > 3000:
    place = "Hotel"
    budget *= 0.90
    if season == "Summer":
        location = "Alaska"
    elif season == "Winter":
        location = "Morocco"

print(f"{location} - {place} - {budget:.2f}")