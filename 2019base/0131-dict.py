lables = {
    'phone': 'asdf',
    'addr': 'sdf'
}

b = lables.get('addrb', {})
print(b)
a = lables.keys()
print(a)
a = lables.items()
print(a)
lables.pop('addr')
print(lables)