# Дано множество A из N точек (N > 2, точки заданы своими координатами x, у). Найти
# наибольший периметр треугольника, вершины которого принадлежат различным
# точкам множества A, и сами эти точки (точки выводятся в том же порядке, в котором
# они перечислены при задании множества A).
# Расстояние R между точками с координатами (x1, y1) и (x2, у2) вычисляется по формуле:
# R = √(x2 – x1)2 + (у2 – y1)2
# Для хранения данных о каждом наборе точек следует использовать по два список: первый
# список для хранения абсцисс, второй — для хранения ординат.
import random
from math import sqrt, ceil
def formula(C1,D1,C2,D2):
    R = sqrt(((C2-C1)**2)+((D2-D1)**2))
    R = ceil(R)
    return R
def peri(chislo1,chislo2,chislo3):
    sum = chislo1+chislo2+chislo3
    return sum
A = [] # cписок для точек
PER = [] # список для периметров
X = [] # список для координат x
Y = [] # список для координат y
N = 4
print('В множестве А количество точек:', N)
F = N
names = 1
while F > 0:
    F -= 1
    A.append(names)
    names += 1
print('Точки в множестве:', A)
count = N
while count > 0:
    count -= 1
    X.append(random.randint(-10, 10))
    Y.append(random.randint(-10, 10))
print('Координаты по X:', X)
print('Координаты по Y:', Y)
count = 0
a = formula(X[0],Y[0],X[1],Y[1])
b = formula(X[1], Y[1], X[2], Y[2])
c = formula(X[2],Y[2],X[0],Y[0])
PER.append(peri(a,b,c))
a = formula(X[0],Y[0],X[1],Y[1])
b = formula(X[1], Y[1], X[3], Y[3])
c = formula(X[3],Y[3],X[0],Y[0])
PER.append(peri(a,b,c))
a = formula(X[1],Y[1],X[2],Y[2])
b = formula(X[2], Y[2], X[3], Y[3])
c = formula(X[3],Y[3],X[1],Y[1])
PER.append(peri(a,b,c))
a = formula(X[2],Y[2],X[3],Y[3])
b = formula(X[3], Y[3], X[0], Y[0])
c = formula(X[0],Y[0],X[2],Y[2])
PER.append(peri(a,b,c))
PER.sort(key=None, reverse=True)
print('Cписок периметров:', PER)
print('Наибольший периметр',PER[0])
