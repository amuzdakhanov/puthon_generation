"""
На вход программе подаются два натуральных числа n и m, каждое на отдельной строке — количество строк и столбцов в матрице.
Далее вводятся сами элементы матрицы — слова, каждое на отдельной строке; подряд идут элементы сначала первой строки, затем второй, и т.д.

Напишите программу, которая считывает элементы матрицы один за другим,
выводит их в виде матрицы, выводит пустую строку, и снова ту же матрицу,
но уже поменяв местами строки со столбцами: первая строка выводится как первый столбец, и так далее.

Формат входных данных
На вход программе подаются два числа nnn и mmm — количество строк и столбцов в матрице, далее идут mxn слов, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести считанную матрицу, за ней пустую строку, и ту же матрицу,
но поменяв местами строки со столбцами. Элементы матрицы разделять одним пробелом.
"""

def print_matrix(matrix, n, m):
    for r in range(n):
        for c in range(m):
            print(matrix[r][c], end=' ')
        print()
def print_matrix_col(matrix, n, m):
    for c in range(m):
        for r in range(n):
            print(matrix[r][c], end=' ')
        print()

n, m = int(input()), int(input())
matrix = []

for i in range(n):
    row = []
    for j in range(m):
        row.append(input())
    matrix.append(row)


print_matrix(matrix, n, m)
print()
print_matrix_col(matrix, n, m)