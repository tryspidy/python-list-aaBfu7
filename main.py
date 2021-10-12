a1 = [1, 'x', 'y']
a2 = [1, 'x', 'y']
a3 = [1, 'x', 'y']

b = [2, 3]

a1.append(b)
a2.insert(3, b)
a3.extend(b)

print(a1)
print(a2)
print(a3