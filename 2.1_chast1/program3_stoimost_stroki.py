
"""
Дана строка текста. 
Напишите программу для подсчета стоимости строки, исходя из того, что один любой символ (в том числе пробел) стоит 60 копеек. 
Ответ дайте в рублях и копейках в соответствии с примерами.

Формат входных данных
На вход программе подается строка текста.

Формат выходных данных
Программа должна вывести стоимость строки.

Sample Input 1:
Привет, как дела?!

Sample Output 1:
10 р. 80 коп.
"""
"""
total = len(s)*60
rubles = total//100
kopeikas = total%100
"""
def calculate_string_symbols(s):
    return len(s)

def calculate_cost_of_symbols(length):
    return length*60

def devide_rubles_and_kopeiks(total):
    rubles = total//100
    kopeiks = total % 100 
    print(rubles,'р.', kopeiks,'коп.')

s = input()

devide_rubles_and_kopeiks(calculate_cost_of_symbols(calculate_string_symbols(s)))