# Из исходного текстового файла (Dostoevsky.txt) выбрать блок информации за 1857
# год и поместить ее в новый текстовый файл.
import re
f = open('Dostoevsky.txt', encoding='utf-8')
text = f.read()
p = re.compile(r"После .*", re.M)
f = open('novi.txt', 'w')
f.writelines(p.findall(text))
f.close