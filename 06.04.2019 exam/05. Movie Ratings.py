import sys
number_of_films = int(input())
highest_rating = -sys.maxsize
lowest_rating = sys.maxsize
sum_ratings = 0
highest_rating_film = ''
lowest_rating_film = ''
for i in range(1, number_of_films + 1):
    name_of_film = input()
    rating = float(input())
    sum_ratings += rating
    if rating > highest_rating:
        highest_rating_film = name_of_film
        highest_rating = rating
    if rating < highest_rating:
        lowest_rating_film = name_of_film
        lowest_rating = rating

average_rating = sum_ratings / number_of_films
print(f"{highest_rating_film} is with highest rating: {highest_rating:.1f}")
print(f"{lowest_rating_film} is with lowest rating: {lowest_rating:.1f}")
print(f"Average rating: {average_rating:.1f}")
