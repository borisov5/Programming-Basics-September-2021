number_of_films = int(input())
current_rating = 0
average_rating = 0
for i in range(number_of_films):
    film_name = input()
    rating = float(input())
    average_rating += rating
    if rating > current_rating:
        film_with_highest_rating = film_name
        highest_rating = rating
    elif rating < current_rating:
        film_with_lowest_rating = film_name
        lowest_rating = rating
    current_film_name = film_name
    current_rating = rating


average_rating /= number_of_films
print(f"{film_with_highest_rating} is with highest rating: {highest_rating:.1f}")
print(f"{film_with_lowest_rating} is with lowest rating: {lowest_rating:.1f}")
print(f"Average rating: {average_rating:.1f}")