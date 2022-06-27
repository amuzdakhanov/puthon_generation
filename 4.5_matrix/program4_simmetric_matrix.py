n = int(input())
matrix = []
for i in range(n):
    temp = [int(num) for num in input().split()]
    matrix.append(temp)

print(matrix)

for i in range(n):
    for j in range(n):

