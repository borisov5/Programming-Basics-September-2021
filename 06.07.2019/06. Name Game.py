winner = ''
points_of_winnter = 0
command = input()
while command != "Stop":
    name_of_player = len(command)
    points = 0
    for i in range(name_of_player):
        point = int(input())
        if point == ord(command[0]):
            points += 10
        else:
            points += 2

    if points_of_winnter < points:
        points_of_winnter = points
        winner = command
    command = input()

print(f"The winner is {winner} with {points_of_winnter} points!")