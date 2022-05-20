#1
#print("Hello SoftUni")

#2
#for x in range(1,11):
#	print(x)

#3
#a = int(input())
#b = int(input())
#area = a * b
#print(area)

#4
#inches = float(input('Inches = '))
#centimeters = inches * 2.54
#print('centimeters = ', centimeters)

#5
#name = input()
#print("Hello, " + name + "!")

#6
#first_name = input()
#last_name = input()
#age = int(input())
#town = input()
#print("You are " + first_name + " " + last_name +", a " + str(age) +"-years old person from " + town + ".")

#7
#name = input()
#number_of_projects = int(input())
#time_to_compleate_all_projects = number_of_projects * 3
#print(f"The architect {name} will need {time_to_compleate_all_projects} hours to complete {number_of_projects} project/s.")

#8
#a = int(input("Broqt na opakovkite hrana za kucheta e: "))
#b = int(input("Broqt na opakovkite hrana za kotki e: "))
#hrana_za_kucheta = a * 2.50
#hrana_za_kotki = b * 4
#kraina_suma = hrana_za_kucheta + hrana_za_kotki
#print(f"{kraina_suma} lv.")

#9
#square_meters_for_landscaping = float(input())
#price_for_the_whole_yard = square_meters_for_landscaping * 7.61
#discount = price_for_the_whole_yard * 0.18
#total_sum = price_for_the_whole_yard - discount
#print(f"The final price is : {total_sum} lv.")
#print(f"The discount is: {discount} lv.")


#Закръгляне
#print(round(x, 2))
#или print(%.2f)

#Преобразуване от string в int или float
#parseInt() #parseFloat()

#PRACTICE
#1
#b1 = float(input())
#b2 = float(input())
#h = float(input())
#area = (b1 + b2) * h / 2
#print(f'{area:.2f}')

#2
#a = float(input())
#h = float(input())
#area = a * h / 2
#print(f'{area:.2f}')

#3
#celsius = float(input())
#fahrenheit = celsius * 1.8 + 32
#print(f'{fahrenheit:.2f}')

#4
#price_vegetables = float(input())
#price_fruits = float(input())
#total_vegetables = float(input())
#total_fruits = float(input())
#total_vegetables = total_vegetables * price_vegetables
#total_fruits = total_fruits * price_fruits
#total_cost = total_vegetables + total_fruits
#total_cost = total_cost / 1.94
#rint(f'{total_cost:.2f}')

#05. Training Lab
#length = float(input())
#width = float(input())
#length = length * 100
#width = width * 100
#width = width - 100
#length = length // 120
#width = width // 70
#count_places = length * width
#ount_places = count_places - 3
#print(count_places)

#6
#price_mackerel = float(input())
#price_sprat = float(input())
#kilograms_bonito = float(input())
#kilograms_scad = float(input())
#kilograms_mussels = float(input())
#bonito = price_mackerel + (price_mackerel * 0.60)
#sum_bonito = bonito * kilograms_bonito
#scad = price_sprat + (price_sprat * 0.80)
#sum_scad = scad * kilograms_scad
#price_mussels = 7.50
#sum_mussels = kilograms_mussels * price_mussels
#total_cost = sum_bonito + sum_scad + sum_mussels
#print(f'{total_cost:.2f}')

#7
#x = float(input())
#y = float(input())
#h = float(input())
#side_wall = x * y
#window = 1.5 * 1.5
#two_pages = 2 * side_wall - 2 * window
#back_wall = x * x
#entrance = 1.2 * 2
#total_front_and_back = 2 * back_wall - entrance
#total = two_pages + total_front_and_back
#liters_green_paint = total / 3.4
#print(f'{liters_green_paint:.2f}')
#two_rectangles = 2 * (x * y)
#two_triangles = 2 * (x * h / 2)
#total_roof = two_triangles + two_rectangles
#liters_red_paint = total_roof / 4.3
#print(f'{liters_red_paint:.2f}')

#8
#r = float(input())
#from math import pi
#calculated_area = pi * r ** 2
#calculated_parameter = 2 * pi * r
#print(f'{calculated_area:.2f}')
#rint(f'{calculated_parameter:.2f}')

#9
#weather = str(input())
#if weather == "sunny":
#    print("It's warm outside!")
#else:
#    print("It's cold outside!")

#10
#degrees = float(input())
#if degrees <= 11.9:
#    print("Cold")
#elif degrees <= 14.9:
#    print("Cool")
#elif degrees <= 20:
#    print("Mild")
#elif degrees <= 25.9:
#    print("Warm")
#elif degrees <= 35:
#    print("Hot")
#else:
#    print("unknown")
