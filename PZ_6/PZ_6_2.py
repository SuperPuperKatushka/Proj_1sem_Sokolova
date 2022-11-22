# Дан целочисленный список A размера N. Переписать в новый целочисленный
# список B все четные числа из исходного списка (в том же порядке) и вывести размер
# полученного список B и его содержимое.
import random
A = []
B = []
N = input("Введите размер списка: ")
while type(N) != int:
    try:
        N = int(N)
    except ValueError:
        print('Введите целое число!')
        N = input("Введите размер списка: ")
F = N
while F > 0:
    F -= 1
    A.append(random.randint(-100, 100))
for element in A:
    if element % 2 == 0:
        B.append(element)
    else: continue
count = 0
for element in B:
    count += 1
print('Первоначальный список', A)
print('Список четных чисел', B)
print('Количество элементов в списке', count)