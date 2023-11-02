import re

f = open('row.txt', 'r', encoding='utf-8')
text = f.read()

x = re.findall("ab{2,3}", text)
print(x)