occupied_seats = 0
total_tickets = 0
student_tickets = 0
standard_tickets = 0
kid_tickets = 0

while True:
    occupied_seats = 0
    name_of_film = input()
    if name_of_film == "Finish":
        break
    free_spots = int(input())
    for i in range(free_spots):
        ticket_type = input()
        if ticket_type == "standard":
            standard_tickets += 1
        elif ticket_type == "student":
            student_tickets += 1
        elif ticket_type == "kid":
            kid_tickets += 1
        elif ticket_type == "End":
            break
        total_tickets +=1
        occupied_seats += 1
    percent = occupied_seats / free_spots * 100
    print(f"{name_of_film} - {percent:.2f}% full.")

student_tickets = (student_tickets / total_tickets) * 100
standard_tickets = (standard_tickets / total_tickets) * 100
kid_tickets = (kid_tickets / total_tickets) * 100
print(f"Total tickets: {total_tickets}")
print(f"{student_tickets:.2f}% student tickets.")
print(f"{standard_tickets:.2f}% standard tickets.")
print(f"{kid_tickets:.2f}% kids tickets.")