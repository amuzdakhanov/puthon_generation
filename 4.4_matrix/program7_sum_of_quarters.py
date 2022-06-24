"""
Квадратная матрица разбивается на четыре четверти, ограниченные главной и побочной диагоналями: верхнюю, нижнюю, левую и правую.
Напишите программу, которая вычисляет сумму элементов: верхней четверти; правой четверти; нижней четверти; левой четверти.

Формат входных данных
На вход программе подаётся натуральное число nnn — количество строк и столбцов в матрице, затем элементы матрицы (целые числа) построчно через пробел.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.

Примечание. Элементы диагоналей не учитываются.
Тестовые данные 🟢

Sample Input 1:

4
1 2 3 4
5 6 7 8
3 4 5 6
1 2 3 4

Sample Output 1:

Верхняя четверть: 5
Правая четверть: 14
Нижняя четверть: 5
Левая четверть: 8
"""
def sum_num(matrix,n):
    sum_top = 0
    sum_left = 0
    sum_right = 0
    sum_bottom = 0
    for i in range(n):
        for j in range(n):
            if i < j and i < n-1-j :
                sum_top += matrix[i][j]
            elif i < j and i > n - 1 - j:
                sum_right += matrix[i][j]
            elif i > j and i > n-1-j:
                sum_bottom += matrix[i][j]
            elif i > j and i < n-1-j:
                sum_left +=  matrix[i][j]
    return sum_top,sum_right,sum_bottom,sum_left

n = int(input())
matrix = []
for i in range(n):
    temp = [int(num) for num in input().split()]
    matrix.append(temp)


sum_top,sum_right,sum_bottom,sum_left = sum_num(matrix,n)
print('Верхняя четверть:',sum_top)
print('Правая четверть:',sum_right)
print('Нижняя четверть:',sum_bottom)
print('Левая четверть:',sum_left)
