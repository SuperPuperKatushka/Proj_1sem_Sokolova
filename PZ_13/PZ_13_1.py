# В матрице найти среднее арифметическое положительных элементов, кратных 3.
import random
from functools import reduce
count = 0
dec = []
total = 0
while count < 3:
    a = [random.randint(-10,10) for n in range(0,3)]
    count += 1
    dec.append(a)
print('Матрица: ', dec)
for i in dec:
    nue = list(filter(lambda x: x % 3 == 0, i))
    nue = list(filter(lambda x: x > 0, nue))
    if len(nue) != 0:
        total += reduce(lambda x, y: x+y, nue)
print('Cреднее арифметическое положительных элементов, кратных 3: ', total)