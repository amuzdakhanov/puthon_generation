def greater_than_average(matrix, n):
    total_num = []
    for i in range(n):
        counter = 0
        average = sum(matrix[i])/n
        for j in range(n):
            if matrix[i][j] > average:
                counter += 1
        total_num.append(counter)
    return(total_num)



n = int(input())
matrix = []
for i in range(n):
    temp = [int(num) for num in input().split()]
    matrix.append(temp)
print(*greater_than_average(matrix,n),sep='\n')
