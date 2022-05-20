#1
#usd = float(input())
#bgn = usd * 1.79549
#print(bgn)

#2
#from math import pi
#radians = float(input())
#degrees = radians * 180 / pi
#print(degrees)

#or
#import math
#radians = float(input())
#degrees = radians * 180 / math.pi
#print(degrees)

#3
#depozirana_suma = float(input())
#srok_na_depozita = int(input())
#godishen_lihven_procent = float(input()) / 100
#suma = depozirana_suma + srok_na_depozita * ((depozirana_suma * godishen_lihven_procent) / 12)
#print(suma)

#4
#broi_stranici = int(input())
#stranici = int(input())
#broi_dni = int(input())
#broi_chasove = broi_stranici / stranici / broi_dni
#print(broi_chasove)

#5
#broi_paketi_himikali = int(input())
#broi_paketi_markeri = int(input())
#litri_preparat_za_pochistvane_na_duska = int(input())
#procent_namalenie = int(input())
#a = broi_paketi_himikali * 5.80
#b = broi_paketi_markeri * 7.20
#c = litri_preparat_za_pochistvane_na_duska * 1.20
#d = procent_namalenie / 100
# comment d /= 100
#vsichki_materiali = a + b + c
#cena_s_namalenie = vsichki_materiali - (vsichki_materiali * d)
#print(cena_s_namalenie)

#6
#a = int(input())
#b = int(input())
#c = int(input())
#d = int(input())
#e = ((a + 2) * 1.50 + (b + (b * 10 / 100)) * 14.50 + c * 5 + 0.4)
#f = (e * 30 / 100) * d
#g = e + f
#print(g)

#7
#a = int(input())
#b = int(input())
#c = int(input())
#d = a * 10.35 + b * 12.40 + c * 8.15
#e = d * 20 / 100
#f = 2.50
#g = d + e + f
#print(g)

#8
#a = int(input())
#b = a - (a * 40) / 100
#c = b - (b * 20) / 100
#d = c / 4
#e = d / 5
#obshta_cena = a + b + c + d + e
#print(obshta_cena)

#9
#duljina = int(input())
#shirochina = int(input())
#visochina = int(input())
#procent = float(input())
#a = (duljina * shirochina * visochina) * 0.001
#b = procent / 100
#c = a * (1 - b)
#print(c)

#6
#amount_of_nylon = int(input())
#amount_of_dye = int(input())
#amount_of_thinner = int(input())
#hours = int(input())

#sum_nylon = (amount_of_nylon + 2) * 1.50
#sum_dye = (amount_of_dye + amount_of_dye * 10 / 100) * 14.50
#sum_thinner = amount_of_thinner * 5
#bags = 0.40

#total_materials = sum_nylon + sum_dye + sum_thinner + bags
#sum_foreman = (total_materials * 30) / 100
#sum_foreman = sum_foreman * hours

#total_costs = total_materials + sum_foreman
#print(total_costs)


#6
#amount_of_nylon = int(input())
#amount_of_dye = int(input())
#amount_of_thinner = int(input())
#hours = int(input())

#sum_nylon = (amount_of_nylon + 2) * 1.50
#sum_dye = (amount_of_dye + amount_of_dye * 0.1) * 14.50
#sum_thinner = amount_of_thinner * 5
#bags = 0.40

#total_materials = sum_nylon + sum_dye + sum_thinner + bags
#sum_foreman = (total_materials * 30) / 100
#sum_foreman = sum_foreman * hours

#total_costs = total_materials + sum_foreman
#print(total_costs)
