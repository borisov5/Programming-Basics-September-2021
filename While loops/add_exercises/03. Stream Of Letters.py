import string
count_c = 0
count_o = 0
count_n = 0
word = ''
final = ""
command = input()
while command != "End":
    if command in string.ascii_letters:
        if command == "c" and count_c == 0:
            count_c += 1
        elif command == "o" and count_o == 0:
            count_o += 1
        elif command == "n" and count_n == 0:
            count_n += 1
        else:
            word += command

        if count_c == 1 and count_o == 1 and count_n == 1:
            final += word + " "
            count_c, count_n, count_o = 0, 0, 0
            word = ""
    command = input()
print(final)
