from math import sqrt
a1 = 7
b1 = 2
c1 = 8
def triangle_perimeter(a = a1, b = b1, c = c1):
    P = a + b + c
    return(P)
def triangle_area(a = a1, b = b1, c = c1):
    p = (a + b + c) / 2
    S = sqrt(p*(p-a)*(p-b)*(p-c))
    return(S)
