import random

lower = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
upper = 'abcdefghijklmnopqrstuvwxyz'
numbers = '0123456789'
symbols = '[]{}(),./-_'

all_combinations = lower + upper + numbers + symbols
length = 10
password = ''.join(random.sample(all_combinations, length))
print(password)
