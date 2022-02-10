# -*- coding: utf-8 -*-

# %%
i = 0
while i < 5:
    print(i)
    i += 1 
    
# %%

n = 0
while True:
    print(n)
    if n >= 10:
        break
    n += 1
    
# %%
while True:
    name = input('Podaj swoje imie: ')
    if len(name) >= 3 and name.isalpha():
        break
print('Cześć {}'.format(name))

# %%
n = 0

while n < 20:
    n += 1
    if n % 2 == 0:
        continue
    print(n)
    
# %%
lista_do_przeszukania = [12, 53, 13, 63, 34]
flaga = False

idx = 0
while idx < len(lista_do_przeszukania):
    print(lista_do_przeszukania[idx])
    idx += 1
    
# %%
lista_do_przeszukania = [12, 53, 13, 63, 34]
flaga = False
wartosc = 6

idx = 0
while idx < len(lista_do_przeszukania):
    if lista_do_przeszukania[idx] == wartosc:
        flaga = True
    idx += 1
    
if flaga:
    print('Znaleziono element {}'.format(wartosc))
else:
    print('Nie znaleziono elementu {}'.format(wartosc))
    
# %%
lista_do_przeszukania = [12, 53, 13, 63, 34]
flaga = False
wartosc = 6

idx = 0
while idx < len(lista_do_przeszukania):
    if lista_do_przeszukania[idx] == wartosc:
        flaga = True
    idx += 1
    
if not flaga:
    lista_do_przeszukania.append(wartosc)
    
# %% Ćwiczenie 10
numbers = [23, 12, 53, 13, 65, 1, 45]
i = 0
while i < len(numbers):
    if numbers[i] == 13:
        print('Znaleziono')
        break
    i += 1