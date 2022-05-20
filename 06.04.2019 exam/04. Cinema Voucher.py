value_of_vaucher = int(input())
command = input()
film_price = 0
sum_tickets = 0
other_things = 0
while command != "End":
    if len(command) > 8:
        first_char = command[0]
        second_char = command[1]
        film_price = ord(first_char) + ord(second_char)
        if film_price <= value_of_vaucher:
            value_of_vaucher -= film_price
            sum_tickets += 1
        else:
            break
    elif len(command) <= 8:
        first_char = command[0]
        film_price = ord(first_char)
        if film_price <= value_of_vaucher:
            value_of_vaucher -= film_price
            other_things += 1
        else:
            break
    command = input()
print(f"{sum_tickets}")
print(f"{other_things}")