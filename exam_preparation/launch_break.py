import math
name_of_serial = input()
episode_duration = int(input())
duration_of_break = int(input())

time_for_lunch = duration_of_break * 1 / 8
time_for_rest = duration_of_break * 1 / 4
time_left = duration_of_break - time_for_lunch - time_for_rest

if time_left >= episode_duration:
    free_time = time_left - episode_duration
    print(f"You have enough time to watch {name_of_serial} and left with {math.ceil(free_time)} minutes free time.")
else:
    needed_time = episode_duration - time_left
    print(f"You don't have enough time to watch {name_of_serial}, you need {math.ceil(needed_time)} more minutes.")