a = {1, 2}
a.add(3)

b = a.copy()
b.add(4)

c = a.intersection(b)
c_listed = list(c)
print(c_listed)