# -*- coding: utf-8 -*-

empty_dict = dict() # tworzenie słownika
print(empty_dict)

d = {} # tworzenie słownika
print(type(d))

e = set() # tworzenie zboiru

# %%
pol_to_eng = {'jeden':'one' , 'dwa':'two', 'trzy':'three'}

name_to_digit = {'jeden':1, 'dwa':2, 'trzy':3}

# %%
name_to_digit = {0:1, 1:2, 2:3}

len(name_to_digit)

# %%
# dict = {'key1':'value1', 'key2':'value2'}

# %%
pol_to_eng['cztery'] = 'four'

# %%
pol_to_eng.clear()

# %%
pol_to_eng_copied = pol_to_eng.copy()

# %%
list(pol_to_eng.keys())

# %%
list(pol_to_eng.values())

# %%
list(pol_to_eng.items()) # Lista tupli

# %%
pol_to_eng['jeden']
# pol_to_eng['zero']

# %%
pol_to_eng.get('zero', 'NaN')

# %%
#pol_to_eng.pop('dwa')
pol_to_eng.popitem()

# %%
pol_to_eng.update({'dwa':2})

# %% Ćwiczenie 7
num_to_pow = {1:1, 2:4, 3:9, 4:16, 5:25}
print(num_to_pow)

# %% Ćwiczenie 8
capitals = {'Polska':'Warszawa', 'Niemcy':'Berlin', 'Czechy':'Praga'}
capitals['Włochy'] = 'Rzym'
cap_list = list(capitals.values())
cap_list.sort()
print(cap_list)