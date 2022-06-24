"""
Нижняя половина квадрата  максимум вывести
 Sample Input 1:

3
1 4 5
6 7 8
1 1 6

Sample Output 1:

7
"""

def max_num(matrix,n):
    max_n = matrix[0][0]
    for i in range(n):
        for j in range(n):
            if i >= j and matrix[i][j] > max_n:
                max_n = matrix[i][j]
    return max_n
n = int(input())
matrix = []
for i in range(n):
    temp = [int(num) for num in input().split()]
    matrix.append(temp)


print(max_num(matrix,n))