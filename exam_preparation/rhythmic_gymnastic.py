country = input()
device = input()
difficult = 0
score = 0
if country == "Russia":
    if device == "ribbon":
        difficult = 9.1
        score = 9.4
    elif device == "hoop":
        difficult = 9.3
        score = 9.8
    elif device == "rope":
        difficult = 9.6
        score = 9
elif country == "Bulgaria":
    if device == "ribbon":
        difficult = 9.6
        score = 9.4
    elif device == "hoop":
        difficult = 9.55
        score = 9.75
    elif device == "rope":
        difficult = 9.5
        score = 9.4
elif country == "Italy":
    if device == "ribbon":
        difficult = 9.2
        score = 9.5
    elif device == "hoop":
        difficult = 9.45
        score = 9.35
    elif device == "rope":
        difficult = 9.7
        score = 9.15

grade = score + difficult
print(f"The team of {country} get {grade:.3f} on {device}.")
percent = ((20 - grade) / 20) * 100
print(f"{percent:.2f}%")