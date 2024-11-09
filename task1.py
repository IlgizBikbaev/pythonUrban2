import random

result = ''

def stone_field():
    number = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    number = random.choice(number)
    return number

number = stone_field()
print('Ваше число:', number)

for i in range(1, number):
    for j in range(i+1, number):
        if i >= j:
            continue
        if number % (i+j) == 0:
            result += str(i) + str(j)

print('необходимый код:', result)


