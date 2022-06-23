"""
На вход программе подаются два натуральных числа n и m, каждое на отдельной строке — количество строк и столбцов в матрице.
Далее вводятся сами элементы матрицы — слова, каждое на отдельной строке; подряд идут элементы сначала первой строки, затем второй, и т.д.

Напишите программу, которая сначала считывает элементы матрицы один за другим, затем выводит их в виде матрицы.

Формат входных данных
На вход программе подаются два числа n и m — количество строк и столбцов в матрице, далее идут  n x m слов, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести считанную матрицу, разделяя ее элементы одним пробелом.
Sample Input 1:
4
2
и
швец
и
жнец
и
на
дуде
игрец

Sample Output 1:
и швец
и жнец
и на
дуде игрец
"""
def print_matrix(matrix, n, m):
    for r in range(n):
        for c in range(m):
            print(matrix[r][c], end=' ')
        print()

n = int(input())
m = int(input())
matrix = [[0]*m for i in range(n)]

for i in range(n):
    for j in range(m):
        matrix[i][j] = input()

print_matrix(matrix,n,m)

"""
n, m = int(input()), int(input())
matrix = []

for i in range(n):
    row = []
    for j in range(m):
        row.append(input())
    matrix.append(row)

for i in range(n):
    for j in range(m):
        print(matrix[i][j], end=' ')
    print()
"""