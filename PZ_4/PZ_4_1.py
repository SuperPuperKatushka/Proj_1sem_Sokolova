# Дано целое число N (>0). Найти сумму 1 + 1/2 + 1/3 + ... + 1/N
N = input("Введите целое число больше нуля: ")
while type(N) != int:
    try:
        N = int(N)
    except ValueError:
        print('Введите целое число!')
        N = input("Введите целое число больше нуля: ")
k = 1
a = 0
while k <= N:
    s = 1/k
    a = a + s
    k += 1
print(a)
