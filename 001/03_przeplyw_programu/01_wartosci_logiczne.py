# -*- coding: utf-8 -*-

val_1 = True
val_2 = False

# %%
print(val_1)
print(type(val_1))

# %% koniunkcja
True and True
True and False
False and True
False and False

# %% alternatywa
True and True
True and False
False and True
False and False

# %% negacja
True
not True
not False

# %%
bool('python')
bool('')
bool(0)
bool(3.14)
bool(0.0)
bool('0.0')
bool({})
bool(set())
bool(list())
bool(tuple())
bool({'key':'val'})

# %% Ćwiczenie 1
print(bool(' '))
print(bool(''))
print(bool('1'))
print(bool(['', '']))
