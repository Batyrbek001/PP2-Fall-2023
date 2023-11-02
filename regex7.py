import re

f = open('row.txt', 'r', encoding='utf-8')
text = f.read()

x = re.sub(r'_', lambda match: match.group(1).upper(), text)
print(x)