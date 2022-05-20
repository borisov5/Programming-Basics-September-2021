number_of_people = int(input())
number_nights = int(input())
number_cards = int(input())
number_tickets = int(input())

nights = number_nights * 20
transport_cards = number_cards * 1.60
museum_tickets = number_tickets * 6
sum_for_one_person = nights + transport_cards + museum_tickets
sum_all_grup = sum_for_one_person * number_of_people
total_costs = sum_all_grup + sum_all_grup * 0.25

print(f"{total_costs:.2f}")