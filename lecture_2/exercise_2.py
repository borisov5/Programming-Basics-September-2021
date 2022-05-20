#1
#first_competitor = int(input())
#second_competitor = int(input())
#third_competitor = int(input())
#total_time = first_competitor + second_competitor + third_competitor
#seconds = total_time % 60
#minutes = total_time // 60
#if seconds < 10:
#    print(f'{minutes}:0{seconds}')
#else:
#    print(f'{minutes}:{seconds}')

#2
#number = int(input())
#bonus = 0
#if number <= 100:
#    bonus = 5
#elif 100 < number <= 1000:
#    bonus = number * 0.2
#else:
#    bonus = number * 0.1
#if number % 2 == 0:
#    bonus += 1
#elif number % 10 == 5:
#    bonus += 2
#print(bonus)
#print(bonus + number)

#3
#hours = int(input())
#minutes = int(input())
#minutes = minutes + 15
#total_time = minutes + hours * 60
#hours = total_time // 60
#hours = hours % 24
#minutes = total_time % 60
#if minutes < 10:
#    print(f'{hours}:{minutes:02d}')
#else:
#    print(f'{hours}:{minutes}')

#4
#import math
#trip_price = float(input())
#count_puzzles = int(input())
#sum_dolls = int(input())
#sum_bears = int(input())
#sum_minions = int(input())
#sum_trucks = int(input())
#sum = count_puzzles * 2.60 + sum_dolls * 3 + sum_bears * 4.10 + sum_minions * 8.20 + sum_trucks * 2
#count_toys = count_puzzles + sum_dolls + sum_bears + sum_minions + sum_trucks
#if count_toys >= 50:
#    sum = sum - sum * 0.25
#rent = sum * 0.10
#earnings = sum - rent
#money = earnings - trip_price
#money = abs(money)
#if earnings >= trip_price:
#    print(f'Yes! {money:.2f} lv left.')
#else:
#    print(f'Not enough money! {money:.2f} lv needed.')

#5
#film_budget = float(input())
#sum_statists = int(input())
#price_cloths = float(input())
#import math
#decor = film_budget * 0.10
#if sum_statists > 150:
#    price_cloths = price_cloths - price_cloths * 0.10
#sum_cloths = sum_statists * price_cloths
#film_budget = film_budget - sum_cloths - decor
#if film_budget < 0:
#    film_budget = abs(film_budget)
#    print("Not enough money!")
#    print(f"Wingard needs {film_budget:.2f} leva more.")
#else:
#    print("Action!")
#    print(f"Wingard starts filming with {film_budget:.2f} leva left.")

#6
#record_seconds = float(input())
#distance = float(input())
#time = float(input())
#speed = distance * time
#slow = distance // 15 * 12.5
#total_time = speed + slow
#if record_seconds > total_time:
#   print(f"Yes, he succeeded! The new world record is {total_time:.2f} seconds.")
#else:
#    no_enought_seconds = total_time - record_seconds
#    print(f"No, he failed! He was {no_enought_seconds:.2f} seconds slower.")

#7
#budget = float(input())
#number_videocards = int(input())
#number_processors = int(input())
#number_memories = int(input())
#videocard_price = 250 * number_videocards
#processor_price = videocard_price * 0.35 * number_processors
#memory_price = videocard_price * 0.10 * number_memories
#money = videocard_price + processor_price + memory_price
#if number_videocards > number_processors:
#    money -= money * 0.15
#if budget >= money:
#    money_left = budget - money
#    print(f"You have {money_left:.2f} leva left!")
#else:
#    money_needed = money - budget
#    print(f"Not enough money! You need {money_needed:.2f} leva more!")

#8
#import math
#serial_name = str(input())
#serial_duration = int(input())
#all_time = int(input())
#lunch_time = all_time / 8
#rest_duration = all_time / 4
#time_left = all_time - lunch_time - rest_duration
#if time_left >= serial_duration:
#    time_left -= serial_duration
#    time_left = math.ceil(time_left)
#    print(f"You have enough time to watch {serial_name} and left with {time_left} minutes free time.")
#else:
#    time_needed = serial_duration - time_left
#    time_needed = math.ceil(time_needed)
#    print(f"You don't have enough time to watch {serial_name}, you need {time_needed} more minutes.")
