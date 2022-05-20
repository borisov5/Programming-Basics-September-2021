sum1 = 0
sum2 = 0
n = int(input())
for i in range(0,n):
    a = int(input())
    if  i % 2 == 0:
        sum1 += a
    else:
       sum2 += a
if sum1 == sum2:
    print("Yes")
    print(f'Sum = {sum1}')
else:
    diff = abs(sum1 - sum2)
    print('No')
    print(f'Diff = {diff}')