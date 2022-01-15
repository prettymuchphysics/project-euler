# problem number: 002

N = 4e6

x = 1
y = 2
sum = 0

while y < N:
    if y%2==0:
        sum += y
    tmp = x
    x = y
    y += tmp

print(f'The answer is: {sum}.')