# Составить генератор (yield), который переведет символы строки из нижнего
# регистра в верхний.
def generator(stroka):
    for n in stroka:
         yield n.upper()

stroka = str(input('Введите строку:' ))
result = generator(stroka)

for f in result:
    print(f)
