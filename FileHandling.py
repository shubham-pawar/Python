
f = open('DemoData', 'r')

print(f.readline(), end='')
print(f.readline())

f1 = open('createdByCode', 'w')
f1.write('This is so amazing!')

for data in f:
    f1.write(data)