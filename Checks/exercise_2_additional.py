#1
#volume = int(input())
#pipe_1 = int(input())
#pipe_2 = int(input())
#hours = float(input())
#end_volume = hours * (pipe_1 + pipe_2)
#if volume >= end_volume:
#    full_percent = end_volume / volume * 100
#    percent_pipe_1 = hours * pipe_1 / end_volume * 100
#    percent_pipe_2 = hours * pipe_2 / end_volume * 100
#    print(f"The pool is {full_percent:.2f}% full. "
#      f"Pipe 1: {percent_pipe_1:.2f}%. "
#      f"Pipe 2: {percent_pipe_2:.2f}%.")
#else:
#    litters_more = volume - end_volume
#    litters_more = abs(litters_more)
#    print(f"For {hours:.2f} hours the pool overflows with {litters_more:.2f} liters.")

#2
#holidays = int(input())
#game_in_holydays = holidays * 127
#game_in_workdays = (365 - holidays) * 63
#total_time = game_in_holydays + game_in_workdays
#time = 30000 - total_time
#time = abs(time)
#h = time // 60
#m = time % 60
#if 30000 > total_time:
#    print("Tom sleeps well")
#    print(f"{h} hours and {m} minutes less for play")
#else:
#    print("Tom will run away")
#    print(f"{h} hours and {m} minutes more for play")

#3
#import math
#meters_vineyard = int(input())
#grape_per_suare_meter = float(input())
#needed_liters = int(input())
#number_workers = int(input())
#total_grape = meters_vineyard * grape_per_suare_meter
#wine = total_grape * 0.4 / 2.5
#if wine >= needed_liters:
#    litters_left = wine - needed_liters
#    litters_per_person = litters_left / number_workers
#    litters_left = math.ceil(litters_left)
#    litters_per_person = math.ceil(litters_per_person)
#    wine = math.floor(wine)
#    print(f"Good harvest this year! Total wine: {wine} liters.")
#    print(f"{litters_left} liters left -> {litters_per_person} liters per person.")
#else:
#    not_enought_wine = needed_liters - wine
#    not_enought_wine = math.floor(not_enought_wine)
#    print(f"It will be a tough winter! More {not_enought_wine} liters wine needed.")

#4
#import math
#n = int(input())
#time = str(input())

#taxi_starting_tax = 0.70
#taxi_day_tariff = 0.79
#taxi_night_tariff = 0.90
#bus_tariff = 0.09
#train_tariff = 0.06

#if n >= 100:
#    lower_price = n * train_tariff
#    print(f'{lower_price:.2f}')
#elif n >= 20:
#    lower_price = n * bus_tariff
#    print(f'{lower_price:.2f}')
#else:
#    if time == "day":
#        lower_price = taxi_starting_tax + n * taxi_day_tariff
#        print(f'{lower_price:.2f}')
#    else:
#        lower_price = taxi_starting_tax + n * taxi_night_tariff
#        print(f'{lower_price:.2f}')

#5
#import math
#needed_hours = int(input())
#days = int(input())
#number_employers = int(input())

#working_hours = days * 0.9 * 8
#overtime = number_employers * days * 2
#total_hours = working_hours + overtime
#total_hours = math.floor(total_hours)
#if total_hours >= needed_hours:
#    hours = total_hours - needed_hours
#    print(f"Yes!{hours} hours left.")
#else:
#    hours = needed_hours - total_hours
#    print(f"Not enough time!{hours} hours needed.")

#6
#import math
#number_days = int(input())
#kilograms_food = int(input())
#food_for_dog = float(input())
#food_for_cat = float(input())
#food_for_turtle = float(input())

#needed_food_for_dog = number_days * food_for_dog
#needed_food_for_cat = number_days * food_for_cat
#needed_food_for_turtle = number_days * food_for_turtle / 1000
#total_food = needed_food_for_dog + needed_food_for_cat + needed_food_for_turtle

#if total_food  <= kilograms_food:
#    food_left = kilograms_food - total_food
#    print(f"{math.floor(food_left)} kilos of food left.")
#else:
#    needed_food = total_food - kilograms_food
#    print(f"{math.ceil(needed_food)} more kilos of food are needed.")

#7
#import math
#number_magnolia = int(input())
#number_hyacinths = int(input())
#number_roses = int(input())
#number_cactus = int(input())
#price_gift = float(input())

#sum = number_magnolia * 3.25 + number_hyacinths * 4 + number_roses * 3.5 + number_cactus * 8
#sum = sum - sum * 0.05
#if price_gift <= sum:
#    left_sum = price_gift - sum
#    print(f"She is left with {math.floor(abs(left_sum))} leva.")
#else:
#    needed_money = sum - price_gift
#    print(f"She will have to borrow {math.ceil(abs(needed_money))} leva.")

#8
#fuel_type = str(input().lower())
#litters = float(input())
#if litters >= 25:
#    if fuel_type == "diesel" or fuel_type == "gasoline" or fuel_type == "gas":
#        print(f"You have enough {fuel_type}.")
#    else:
#        print("Invalid fuel!")
#else:
#    if fuel_type == "diesel" or fuel_type == "gasoline" or fuel_type == "gas":
#        print(f"Fill your tank with {fuel_type}!")
#    else:
#        print("Invalid fuel!")

#9
fuel_type = str(input().lower())
litters = float(input())
club_card = str(input().lower())
gasoline = 2.22
diesel = 2.33
gas = 0.93
if club_card == "yes":
    gasoline -= 0.18
    diesel -= 0.12
    gas -= 0.08
    if 20 <= litters <= 25:
        if fuel_type == "gasoline":
            price = gasoline * litters * 0.92
            print(f"{price:.2f} lv.")
        if fuel_type == "diesel":
            price = diesel * litters * 0.92
            print(f"{price:.2f} lv.")
        if fuel_type == "gas":
            price = gas * litters * 0.92
            print(f"{price:.2f} lv.")
    if litters >= 26:
        if fuel_type == "gasoline":
            price = gasoline * litters * 0.9
            print(f"{price:.2f} lv.")
        if fuel_type == "diesel":
            price = diesel * litters * 0.9
            print(f"{price:.2f} lv.")
        if fuel_type == "gas":
            price = gas * litters * 0.9
            print(f"{price:.2f} lv.")
    if litters <= 19:
        if fuel_type == "gasoline":
            price = gasoline * litters
            print(f"{price:.2f} lv.")
        if fuel_type == "diesel":
            price = diesel * litters
            print(f"{price:.2f} lv.")
        if fuel_type == "gas":
            price = gas * litters
            print(f"{price:.2f} lv.")
if club_card == "no":
    if 20 <= litters <= 25:
        if fuel_type == "gasoline":
            price = gasoline * litters * 0.92
            print(f"{price:.2f} lv.")
        if fuel_type == "diesel":
            price = diesel * litters * 0.92
            print(f"{price:.2f} lv.")
        if fuel_type == "gas":
            price = gas * litters * 0.92
            print(f"{price:.2f} lv.")
    if litters >= 26:
        if fuel_type == "gasoline":
            price = gasoline * litters * 0.9
            print(f"{price:.2f} lv.")
        if fuel_type == "diesel":
            price = diesel * litters * 0.9
            print(f"{price:.2f} lv.")
        if fuel_type == "gas":
            price = gas * litters * 0.9
            print(f"{price:.2f} lv.")
    if litters <= 19:
        if fuel_type == "gasoline":
            price = gasoline * litters
            print(f"{price:.2f} lv.")
        if fuel_type == "diesel":
            price = diesel * litters
            print(f"{price:.2f} lv.")
        if fuel_type == "gas":
            price = gas * litters
            print(f"{price:.2f} lv.")
