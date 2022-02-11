# -*- coding: utf-8 -*-

# %%
print(abs(10))
print(abs(-10))

# %%
bool([])
bool('')
bool({})
bool(' ')
bool(True)
bool(False)
bool(12)
bool(0)

# %%
dir(list)
dir(tuple)

# %%
list(enumerate(['pawel', 'python', 'java']))

# %%
eval('1 + 1')

x = 10
eval('x + 13')

# %%

list(filter(abs, [-2, -1, 0, 2]))

# %%
list(filter(bool, ['python', '', 'java']))

# %%
float('3.14')
float(4)
float('dssada')

# %%
type(3.14)

# %%
help(float)
help(int)

# %%
isinstance(1, int)
isinstance(1.0, float)
isinstance('adssadasd', str)
isinstance('', str)

# %%
len('    ')
len('python')
len('')
len([])
len([[3, 4], [4, 5, 6, 7, [5, 5]]])

# %%
list('python')
list(range(10))

# %%
list(map(abs, [-2, -1, 0, 1, 2]))

# %%
names = ['pawel', 'tomek', 'janek']
list(map(str.title, names))

# %%
max([1, 2, 5, 2])
max('pawel')
max('tomek')

min([1, 2, 5, 2])
min('ala')

# %%
pow(2, 4)
2 ** 4

# %%
list(reversed([5, 3, 7]))
list(reversed('python'))

# %%
round(4.324324234, 4)

# %%
str(1)
str(4.33)
str(True)

# %%
sum([3, 4, 5, 3])

# %%
lista_1 = [1, 2, 3]
lista_2 = [4, 5, 6, 7]

list(zip(lista_1, lista_2))

# %%
list(zip('python', 'course'))

# %% Ćwiczenie 1
print(type((1,2,3)))
print(type({1,2,3}))
print(type([1,2,3]))
print(type({1:1, 2:2, 3:3}))
print(type('123'))
print(type(123))