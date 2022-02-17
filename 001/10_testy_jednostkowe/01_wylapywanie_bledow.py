# -*- coding: utf-8 -*-

# %%
1 / 0

# %%
4 + '4'

# %%
int('f')

# %%
float('sd')

# %%
try:
    1 / 0
except:
    print('Nie dzieli się przez 0')
    
# %%
try:
    1 / 0
except ZeroDivisionError:
    print('Nie dzieli się przez 0')
except TypeError:
    print('Zły typ.')
    
# %%
try:
    4 + '4'
except TypeError:
    print('Nie można dodawać tekstu do liczby.')
    
# %%
try:
    int('sd')
except ValueError:
    print('Zły tekst.')
    
# %%
while True:
    try:
        x = int(input('Podaj liczbę: '))
        break
    except ValueError:
        print('Nie wprowadziłeś poprawnej wartości.')
        
# %%
with open('test.txt', 'r') as file:
    for line in file:
        print(line)
# %%
try:
    with open('test.txt', 'r') as file:
        for line in file:
            print(line)
except FileNotFoundError:
    print('Plik nie istnieje.')
    
# %%
raise TypeError('Błąd.')

# %%
raise ValueError('Błąd wartości.')

# %%
def divide(x, y):
    try:
        x = int(x)
        y = int(y)
        return x / y
    except ZeroDivisionError:
        print('Dzielenie przez 0!')
    except ValueError:
        print('Musisz wprowadzić liczbę!')
        
divide(3, 0)
divide('a', '2')
