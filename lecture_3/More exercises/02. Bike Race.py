junior_bicycler = int(input())
senior_bicycler = int(input())
trace_type = input()

junior_price = 0
senior_price = 0

if trace_type == "trail":
    junior_price = 5.50
    senior_price = 7
elif trace_type == "cross-country":
    junior_price = 8
    senior_price = 9.50
elif trace_type == "downhill":
    junior_price = 12.25
    senior_price = 13.75
elif trace_type == "road":
    junior_price = 20
    senior_price = 21.50

tax = junior_bicycler * junior_price + senior_bicycler * senior_price
sum_bicyclers = junior_bicycler + senior_bicycler
if sum_bicyclers >= 50 and trace_type == "cross-country":
    tax *= 0.75
total_cost = tax * 0.95

print(f"{total_cost:.2f}")