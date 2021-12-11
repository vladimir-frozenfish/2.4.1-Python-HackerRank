s = 'Привет! Мир! кАК дЕла?'

s_list = []
for i in s:
    if i.isupper():
        s_list.append(i.lower())
    else:
        s_list.append(i.upper())
s = ''.join(s_list)
print(s)
