"""
На вход программе подается число nnn. Напишите программу, которая создает и
 выводит построчно вложенный список, состоящий из nnn списков [[1], [1, 2], [1, 2, 3], ..., [1, 2, ..., n]].

Формат входных данных
На вход программе подается натуральное число n.

Формат выходных данных
Программа должна вывести построчно указанный вложенный список.
Тестовые данные 🟢

Sample Input 1:

4

Sample Output 1:

[1]
[1, 2]
[1, 2, 3]
"""
n = int(input())
list1 = []
for i in range(1,n+1):
   for j in range(1,i+1):
        mylist = [int(j) for j in range(1,i+1)]
   list1.append(mylist)
print(*list1,sep='\n')
