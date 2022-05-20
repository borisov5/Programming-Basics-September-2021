import sys
max_goals = -sys.maxsize
best_player = ''
hat_trick = False
while True:
    player_name = input()
    if player_name == "END":
        break
    number_goals = int(input())
    if number_goals >= 3:
        hat_trick = True
    if number_goals > max_goals:
        max_goals = number_goals
        best_player = player_name
    if number_goals >= 10:
        break


print(f"{best_player} is the best player!")
if hat_trick:
    print(f"He has scored {max_goals} goals and made a hat-trick !!!")
else:
    print(f"He has scored {max_goals} goals.")