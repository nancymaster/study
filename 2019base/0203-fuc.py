names = ['a', 'v']
b = names
c = names[:]
b[0] = 'n'
print(names)
c[0] = 'b'
print(names)

def init(data):
    data['first'] = {}
    data['middle'] = {}
    data['last'] = {}

def lookup(data, lable, name):
    print('hjk',data[lable])
    print('helll:', end=' ')
    print(data[lable].get(name))
    return data[lable].get(name)

def stor(data, full_name):
    name = full_name.split()
    if len(name) == 2: name.insert(1, '')
    lab = 'first', 'middle', 'last'

    for la, nam in zip(lab, name):
        pep = lookup(data, la, nam)
        print("pep: ", pep)
        if pep:
            pep.append(full_name)
            print('sss:', pep)
        else:
            data[la][nam] = [full_name]
            print('else')

store = {}
init(store)
stor(store, 'mary hase kibh')
lookup(store, 'middle', 'hase')

x for x in seq if x.isalnum()