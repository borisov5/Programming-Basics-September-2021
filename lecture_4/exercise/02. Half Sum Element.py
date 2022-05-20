import sys
n = int(input())
sum = 0
max_number = -sys.maxsize
for i in range(1, n + 1):
    current_number = int(input())
    sum += current_number
    if current_number > max_number:
        max_number = current_number

if max_number == (sum - max_number):
    print("Yes")
    print(f"Sum = {max_number}")
else:
    diff = abs(max_number - (sum - max_number))
    print("No")
    print(f"Diff = {diff}")
