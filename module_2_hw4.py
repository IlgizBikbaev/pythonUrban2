def get_matrix(n, m, value):
    if n <= 0 or m <= 0:
        print('Ошибка ввода: число строк или столбцов должно быть положительным')
    matrix = []
    for i in range(n):
        row = []
        matrix.append(row)
        for j in range(m):
            matrix[i].append(value)
    return matrix

n = int(input('Введите количество строк матрицы: '))
m = int(input('Введите количество столбцов матрицы: '))
value = input('Задайте значение: ')

result = get_matrix(n, m, value)
print(result)