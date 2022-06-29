xy = input()
y = '87654321'.index(xy[1]) # i = 2
x = 'abcdefgh'.index(xy[0]) # j = 1

n = 8
matrix = [['.'] * n for _ in range(n)]
matrix[y][x] = 'N'
for i in range(n):
    for j in range(n):
        if (y-i) * (x-j) == -2 or  (y-i) * (x-j) == 2:
            matrix[i][j] = '*'

for i in matrix:
    print(*i)