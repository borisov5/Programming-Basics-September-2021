number_sold_games = int(input())
heartstone_games = 0
fornite_games = 0
overwatch_games = 0
other_games = 0
for i in range(number_sold_games):
    name_of_game = input()
    if name_of_game == "Hearthstone":
        heartstone_games += 1
    elif name_of_game == "Fornite":
        fornite_games += 1
    elif name_of_game == "Overwatch":
        overwatch_games += 1
    else:
        other_games += 1

percent_heartstone = heartstone_games / number_sold_games * 100
percent_fornite = fornite_games / number_sold_games * 100
percent_overwatch = overwatch_games / number_sold_games * 100
percent_other = other_games / number_sold_games * 100
print(f"Hearthstone - {percent_heartstone:.2f}%")
print(f"Fornite - {percent_fornite:.2f}%")
print(f"Overwatch - {percent_overwatch:.2f}%")
print(f"Others - {percent_other:.2f}%")