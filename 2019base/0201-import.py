from math import sqrt as foobar
print(foobar(4))

a, b, *rest = [1,2,3,4,5]
print(rest)
a, b, *rest = '1232434'
print(rest)
a = '7123456789070'
if a.endswith('9'):
    print('9')
elif a.startswith('7'):
    print('7')
else:
    print('8')

for num in range(1,20,5):
    print(num)

for index, string in enumerate(rest):
    rest[index] = '1'
print(rest)

g = ['alice', 'benh', 'dfhj']
b = ['chir', 'ardhf', 'bob']
letg = {}
for gi in g:
    letg.setdefault(gi[0], []).append(gi)
print(letg)