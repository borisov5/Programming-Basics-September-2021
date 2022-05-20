n_1 = int(input())
n_2 = int(input())
operator = input()

result = 0
even_odd = ''

if operator == "+" or operator == "-" or operator == "*":
    if operator == "+":
        result = n_1 + n_2
        if result % 2 == 0:
            even_odd = "even"
        elif result % 2 == 1:
            even_odd = "odd"
    elif operator == "-":
        result = n_1 - n_2
        if result % 2 == 0:
            even_odd = "even"
        elif result % 2 == 1:
            even_odd = "odd"
    elif operator == "*":
        result = n_1 * n_2
        if result % 2 == 0:
            even_odd = "even"
        elif result % 2 == 1:
            even_odd = "odd"
    print(f"{n_1} {operator} {n_2} = {result} - {even_odd}")
elif operator == "/":
    if n_2 == 0:
        print(f"Cannot divide {n_1} by zero")
    elif n_2 != 0:
        result = n_1 / n_2
        print(f"{n_1} / {n_2} = {result:.2f}")
elif operator == "%":
    if n_2 == 0:
        print(f"Cannot divide {n_1} by zero")
    elif n_2 != 0:
        result = n_1 % n_2
        print(f"{n_1} % {n_2} = {result}")
