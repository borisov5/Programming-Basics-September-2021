number_open_tabs = int(input())
salary = int(input())

for _ in range(number_open_tabs):
    site = input()
    if site == "Facebook":
        salary -= 150
    elif site == "Instagram":
        salary -= 100
    elif site == "Reddit":
        salary -= 50

if salary <= 0:
    print("You have lost your salary.")
else:
    print(int(salary))
