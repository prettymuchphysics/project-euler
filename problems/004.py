# problem number: 004

palindromes = []

for i in range(999, 1, -1):
    for j in range(999, i, -1):
        if str(i*j) == str(i*j)[::-1]:
            palindromes.append(i*j)

answer = max(palindromes)

print(f'The answer is: {answer}.')