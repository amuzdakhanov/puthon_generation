"""
На вход программе подаются два целых числа a и b. Напишите программу, которая выводит:

    сумму чисел a и b;
    разность чисел a и b;
    произведение чисел a и b;
    частное чисел a и b;
    целую часть от деления числа a на b;
    остаток от деления числа a на b;
    корень квадратный из суммы их 10-х степеней:  (a**10 + b**10)**0.5

Формат входных данных
На вход программе подаются два целых числа a и b (b≠0), каждое на отдельной строке.

Формат выходных данных
Программа должна вывести результаты математических операций в соответствии с условием задачи.

Sample Input 1:
3
8

Sample Output 1:
11
-5
24
0.375
0
3
32768.90100384814
"""

def summ (a, b):
    return a+b
def difference (a, b):
    return a-b
def mult (a, b):
    return a*b
def chastnoe(a, b):
    return a/b
def celoe (a, b):
    return a//b
def ostatok (a, b):
    return a%b
def koren(a, b):
    return (a**10 + b**10)**0.5


a, b = int(input()), int(input())

for i in (summ(a,b),difference (a, b),mult(a,b),chastnoe(a,b),celoe(a,b),ostatok(a,b),koren(a,b)):
    print(i)
