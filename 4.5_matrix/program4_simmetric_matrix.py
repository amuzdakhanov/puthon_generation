n = int(input())
matrix = []
for i in range(n):
    temp = [int(num) for num in input().split()]
    matrix.append(temp)

flag = 'YES'
counter = 0
for i in range(n):
    for j in range(n):
        if matrix[i][j] != matrix[j][i] :
            flag = 'NO'
            break
print(flag)