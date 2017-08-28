#dict
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Michael'])

d['Adam'] = 67
print(d)

g = d.get('Thomas', 99)
print(g, d)

d.pop('Bob')
print(d)

#set
s = set([1, 2, 3])
print(s)
s = set([1, 1, 2, 3, 3])
print(s)

s.add(4)
s.add(4)
print(s)

s.remove(4)
print(s)

s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
print(s1 & s2, s1 | s2)
