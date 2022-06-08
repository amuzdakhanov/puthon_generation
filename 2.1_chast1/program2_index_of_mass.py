
"""
Напишите программу для вычисления и оценки индекса массы тела (ИМТ) человека. 
ИМТ показывает весит человек больше или меньше нормы для своего роста. 

"""

def index (a, b):
    return a/b**2
def norm (IMT):
    if 18.5<=IMT<=25:
        return 'Оптимальная масса'
    elif IMT < 18.5:
        return 'Недостаточная масса'
    else:
        return 'Избыточная масса'

mass = float(input())
height = float(input())
    
print(norm(index(mass,height)))