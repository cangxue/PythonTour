

# dict：dict的支持，dict全称dictionary，在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度。
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Michael'])

d['Adam'] = 67
print(d)

g = d.get('Thomas', 99)
print(g, d)

d.pop('Bob')
print(d)

# set：set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key
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