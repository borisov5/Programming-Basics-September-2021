total_sum = int(input())
counter = 0
average_cs = 0
average_cc = 0
successful_payment_with_cash = 0
successful_payment_with_card = 0
command = input()
while True:
    if command == "End":
        print("Failed to collect required money for charity.")
        break
    money = int(command)
    counter += 1
    if counter % 2 == 0 and money >= 10:
        average_cc += money
        total_sum -= money
        successful_payment_with_cash += 1
        print("Product sold!")
    elif counter % 2 == 1 and money <= 100:
        average_cs += money
        total_sum -= money
        successful_payment_with_card += 1
        print("Product sold!")
    else:
        print("Error in transaction!")
    if total_sum <= 0:
        average_cs /= successful_payment_with_cash
        average_cc /= successful_payment_with_card
        print(f"Average CS: {average_cs:.2f}")
        print(f"Average CC: {average_cc:.2f}")
        break
    command = input()
