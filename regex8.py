import re

f = open('row.txt', 'r', encoding='utf-8')
text = f.read()

x = re.findall(r'[A-Z][a-z]*', text)
print(x)