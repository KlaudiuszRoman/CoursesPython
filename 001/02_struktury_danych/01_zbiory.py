# -*- coding: utf-8 -*-

empty_set = set()
print(empty_set)
print(type(empty_set))

# %%
techs = {'python', 'java', 'c++', 'sql'}
print(techs)
print(type(techs))
print(len(techs))

# %%
print(set('python'))
print(set('aaaaaale'))

# %%
print('python' in techs)
print('go' in techs)

# %%
print(dir(set))

# %%
techs.add('sas')
print(techs)

# %%
techs.remove('sas')
print(techs)

# %%
print(techs.pop())

# %%
techs.clear()
print(techs)

# %%
A = {1, 2, 3, 4, 5, 6, 7}
B = {5, 6, 7, 8, 9}
C = {5, 6}

print(C.issubset(A))
print(C.issubset({5, 7}))
print(A.issuperset(C))
print(A.union(B))
print(A.intersection(B))
print(A.symmetric_difference(B))

D = A.copy()
print(D)

## Ćwiczenie 1
x = 'Programowanie w języku Python - od A do Z'
x = x.lower().replace('-', '').replace(' ', '').replace('ę', 'e')
y = set(x)
print(y.__len__())

























