film_name = input()
type_salary = input()
number_tickets = int(input())
ticket_price = 0
if film_name == "A Star Is Born":
    if type_salary == "normal":
        ticket_price = 7.50
    elif type_salary == "luxury":
        ticket_price = 10.50
    elif type_salary == "ultra luxury":
        ticket_price = 13.50
elif film_name == "Bohemian Rhapsody":
    if type_salary == "normal":
        ticket_price = 7.35
    elif type_salary == "luxury":
        ticket_price = 9.45
    elif type_salary == "ultra luxury":
        ticket_price = 12.75
elif film_name == "Green Book":
    if type_salary == "normal":
        ticket_price = 8.15
    elif type_salary == "luxury":
        ticket_price = 10.25
    elif type_salary == "ultra luxury":
        ticket_price = 13.25
elif film_name == "The Favourite":
    if type_salary == "normal":
        ticket_price = 8.75
    elif type_salary == "luxury":
        ticket_price = 11.55
    elif type_salary == "ultra luxury":
        ticket_price = 13.95
income = number_tickets * ticket_price
print(f"{film_name} -> {income:.2f} lv.")