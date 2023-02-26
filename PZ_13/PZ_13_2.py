# В матрице элементы строки N (N задать с клавиатуры) увеличить на 3.
import random

count = 0
dec = []
while count < 3:
    a = [random.randint(-10,10) for n in range(0,2)]
    count += 1
    dec.append(a)
print('Матрица: ', dec)
print('Добавьте третью строку')
for i in range(0,3):
    N = input(f'Введите {i+1} элемент')
    while type(N) != int:
        try:
            N = int(N)
        except ValueError:
            print('Введите целое число!')
            N = input(f'Введите {i+1} элемент')
    dec[i].append(N*3)
print('Матрица: ', dec)
