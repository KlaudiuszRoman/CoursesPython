# -*- coding: utf-8 -*-

print('Pprogram uruchomiony...')
print("""Włam  się do systemu, zgadując dwucyfrowy pin.
Numer pin składa się z cyfr: 0, 1, 2.""")
pin = input('Wprowadź numer pin: ')

if pin == '21':
    print('Brawo! Złamałeś system.')
elif pin == '20':
    print('Byłeś blisko!')
else:
    print('Nie zgadłeś.')
    
# %%
pin = int(input('Wprowadź numer pin: '))
print(type(pin))

if pin == 21:
    print('Brawo! Złamałeś system.')
elif pin == 20:
    print('Byłeś blisko!')
else:
    print('Nie zgadłeś.')
    
# %%
bool(0)

# %%
string = ' '

if string:
    print('Niepusty ciąg znaków')
else:
    print('Pusty ciąg znaków')
    
# %%
number = 4.4

if number:
    print('Liczna niezerowa!')
else:
    print('Zeeeero!')
    
# %%
default_flag = False

if not default_flag:
    print('Nie doszło do default')
else:
    print('Doszło')
    
# %% Ćwiczenie 3
v = 55
if v > 50:
    print('Zwolnij!')
else:
    print('Tak trzymaj!')
    
# %%
saldo = -10000
klient_zweryfikowany = False
if saldo > 0 and klient_zweryfikowany:
    print('Możesz wypłacić gotówkę.')
else:
    print('Nie możesz wypłacić gotówki.')
    
# %%
saldo = 10000
klient_zweryfikowany = True

amount = int(input('Ile chcesz wypłacić gotówki: '))
if saldo > 0 and klient_zweryfikowany and saldo >= amount:
    print('Możesz wypłacić gotówkę.')
else:
    print('Nie możesz wypłacić gotówki. \
          Brakuje Ci {}'.format(amount - saldo))
# %% Ćwiczenie 4
fakt = 'python jest łatwy i przyjemny'
fakt_list = list(fakt)
fakt_unique_set = set(fakt_list)
if len(fakt_unique_set) < 20:
    print('Mniej niż 20 unikalnych znaków')

# %%
name = 'ython'

if 'p' in name:
    print('Znaleziono p')
else:
    print('Nie znaleziono p')
    
# %%
tech = 'python'
if tech == 'python':
    flag = 'Doby wybór'
else:
    flag = 'Poszukaj czegoś lepszego'
    
# %%
# x if [warunek] else y
tech = 'sas'
flag = 'Dobry wybór' if tech == 'python' else 'Poszukaj czegoś lepszego'

# %% Ćwiczenie 5
text = 'sfdvjklncdnskjccbnksjdnckjsdsnckjnsdkjnckjsnkjlcnqdlknwsx'
if 'q' in text:
    print('Zawiera')
else:
    print('Nie zawiera')