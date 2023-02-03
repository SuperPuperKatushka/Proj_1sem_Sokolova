# В последовательности их N чисел (N –четное) в первой ее половине найти
# произведение элементов меньших 0.
import random
from functools import reduce
N = 6
F = N
A = []
A1 = []
while F > 0:
    F -= 1
    A.append(random.randint(-100, 100))
print('Последовательность: ', A)
a = int(len(A)/2)
count = 0
while count < a:
    A1.append(A[count])
    count += 1
A2 = list(filter(lambda x: x < 0, A1))
try:
    result = reduce(lambda x,y: x*y, A2)
    print('Произведение элементов меньше нуля в первой половине:', result)
except TypeError:
    print('Все элементы в первой половине положительные')