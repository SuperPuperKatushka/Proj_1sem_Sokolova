# Из предложенного текстового файла (text18-27.txt) вывести на экран его содержимое,
# количество пробельных символов. Сформировать новый файл, в который поместить текст
# в стихотворной форме предварительно поставив последнюю строку фразой введенной
# пользователем.
f = open('text18-27.txt', encoding='UTF-8')
print('Содержимое файла:')
print(f.read())
f.close()
count = 0
for i in open('text18-27.txt', encoding='UTF-8'):
    for j in i:
        if (j == " "):
            count = count + 1
print('Количество пробельных символов:', count)
a = input('Введите последнюю строку:')
f1 = open('text18-27-1.txt', 'w', encoding='UTF-8')
count = 0
for i in open('text18-27.txt', encoding='UTF-8'):
    f1.writelines(i)
    count = count + 1
    if count == 7:
        f1.write('\n')
        f1.writelines(a)