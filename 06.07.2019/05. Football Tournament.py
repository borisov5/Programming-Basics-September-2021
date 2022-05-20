name_of_football_team = input()
number_played_games = int(input())
points = 0
win_games = 0
equal_games = 0
loss_games = 0
for i in range(number_played_games):
    result = input()
    if result == "W":
        points += 3
        win_games += 1
    elif result == "D":
        points += 1
        equal_games += 1
    elif result == "L":
        loss_games += 1

if number_played_games <= 0:
    print(f"{name_of_football_team} hasn't played any games during this season.")
else:
    percent_win_games = win_games / number_played_games * 100
    print(f"{name_of_football_team} has won {points} points during this season.")
    print("Total stats:")
    print(f"## W: {win_games}")
    print(f"## D: {equal_games}")
    print(f"## L: {loss_games}")
    print(f"Win rate: {percent_win_games:.2f}%")
