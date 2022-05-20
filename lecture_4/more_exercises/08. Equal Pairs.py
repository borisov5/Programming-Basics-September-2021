number_of_iteration = int(input())
last_value = 0
current_value = 0
diff = 0
for x in range(number_of_iteration):
    num_a = int(input())
    num_b = int(input())
    current_value = num_a + num_b
    if current_value != last_value and x > 0:
        diff = abs(current_value - last_value)
    last_value = current_value
if diff != 0:
    print(f'No, maxdiff={diff}')
else:
    print(f'Yes, value={current_value}')