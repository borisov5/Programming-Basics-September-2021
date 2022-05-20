import math
number_of_tournament = int(input())
starting_points = int(input())
tournament_points = 0
wins = 0
for i in range(number_of_tournament):
    stage_of_tournament = input()
    if stage_of_tournament == "W":
        tournament_points += 2000
        wins += 1
    elif stage_of_tournament == "F":
        tournament_points += 1200
    elif stage_of_tournament == "SF":
        tournament_points += 720
final_points = starting_points + tournament_points
average_points = tournament_points / number_of_tournament
percent = wins / number_of_tournament * 100

print(f"Final points: {final_points}")
print(f"Average points: {math.floor(average_points)}")
print(f"{percent:.2f}%")
