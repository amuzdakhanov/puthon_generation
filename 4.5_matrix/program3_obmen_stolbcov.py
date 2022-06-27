"""
Напишите программу, которая меняет местами столбцы в матрице.

Формат входных данных
На вход программе на разных строках подаются два натуральных числа n и m — количество строк и столбцов в матрице,
затем элементы матрицы построчно через пробел, затем числа i и j — номера столбцов, подлежащих обмену.

Формат выходных данных
Программа должна вывести указанную таблицу с замененными столбцами.

Sample Input 1:
3
4
11 12 13 14
21 22 23 24
31 32 33 34
0 1

Sample Output 1:
12 11 13 14
22 21 23 24
32 31 33 34
"""
def print_matrix(matrix, n, m):
    for r in range(n):
        for c in range(m):
            print(matrix[r][c], end=' ')
        print()


n,m = int(input()), int(input())


matrix = []
for i in range(n):
    tmp = input().split()
    for j in range(m):
        tmp[j] = int(tmp[j])
    matrix.append(tmp)

rows = input().split()
for i in range(len(rows)):
    rows[i]=int(rows[i])
c1 = min(rows)
c2 = max(rows)


for i in range(n):
    for j in range(m):
            matrix[i][c1], matrix[i][c2] = matrix[i][c2],  matrix[i][c1]
print_matrix(matrix, n, m)

"""
n, m = int(input()), int(input())
matrix = [input().split() for _ in range(n)]
col1, col2 = [int(i) for i in input().split()]

for i in range(n):
    matrix[i][col1], matrix[i][col2] = matrix[i][col2], matrix[i][col1]

for row in matrix:
    print(*row)
"""
