# problem number: 001

N = 1000

sum = 0
for i in range(N):
    sum += i if (i%3==0 or i%5==0) else 0

print(f'The answer is: {sum}.')