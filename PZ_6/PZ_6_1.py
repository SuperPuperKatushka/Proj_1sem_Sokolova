# 1. Дан список A размера N. Найти минимальный элемент из его элементов с четными
# номерами: A2, A4, A6, .... .
import random
A = []
A1 = []
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
index = 1
while index < N:
    if index % 2 == 0:
        A1.append(A[index])
    index += 1
print('Первоначальный список', A)
A1.sort(key=None, reverse=False)
element = A1[0]
print('Список с четными номерами элементов', A1)
print('Минимальный элемент с четным номером', element)