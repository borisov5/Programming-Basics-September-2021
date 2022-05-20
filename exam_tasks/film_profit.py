film_name = input()
number_of_days = int(input())
number_tickets = int(input())
price_of_ticket = float(input())
percent_profit = int(input())

day_sum_tickets = number_tickets * price_of_ticket
profit_for_all_days = day_sum_tickets * number_of_days
percent_for_cinema = profit_for_all_days * percent_profit / 100
profit = profit_for_all_days - percent_for_cinema
print(f"The profit from the movie {film_name} is {profit:.2f} lv.")