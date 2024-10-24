numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []


for i in numbers:
    k = 0
    if i == 1:
        continue
    for j in range(1, i + 1):
        if i % j == 0 and i != j and j != 1:
            k += 1
            not_primes.append(i)
            break
    if k == 0:
        primes.append(i)

print('Простые числа: ', primes)
print('Составные числа: ', not_primes)

