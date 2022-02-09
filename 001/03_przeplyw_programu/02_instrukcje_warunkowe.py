# -*- coding: utf-8 -*-

# %%
version = 3.7
print(version)

# %%
version > 3
version <= 3

# %%
number = 1200
number > 1000

number == 1200
number == 1000

number != 1200
number != 1000

# %%
# if [warunek]:
#    [instrukcje]

# %%
if 8 > 10:
    print('Tak')

# %%
a = 88
if a > 10:
    print('a > 10')
    
# %%
a = 22
if a> 10:
    print('a > 10')
else:
    print('a <= 10')
    
# %%
age = 18

if age < 18:
    print('Nie masz uprawnień.')
else:
    print('Dostępo przyznany.')
    
# %%
age = 12

if age == 18:
    print('Masz 18 lat!')
elif age < 18:
    print('Nie masz uprawnień')
else:
    print('Dostęp przyznany.')
    
# %%
age = int(input('Podaj swój wiek: '))

if age == 18:
    print('Masz 18 lat!')
elif age < 18:
    print('Nie masz uprawnień')
elif age > 18:
    print('Dostęp przyznany.')
    
# %% Ćwiczenie 2
x = 10
if x > 0:
    print('Zmienna x większa od zera')