# -*- coding: utf-8 -*-

# komentarz

# %%
print(2 + 2)
# %%
print(3 * 3)

# %%

print(3 + 2 * 2)
print(4 - 2 * 2)

# %%
10 / 3
4 / 2

# %%
10 // 3
7 // 6

# %%
2 ** 5

# %%
10 % 3
12 % 5
10 % 2

# %%
(10 - 2 ** 3) * 10

# %%
a = 10
b = 20

c = a * b
print(c)

# %%
print('love python')
"love python"

# %%
print("It's the best!")

# %%
print('It\'s the best!')

# %%
print('Python 3.9')

# %%
print('Python\n3.9')

# %%
print("""Python
3.7""")

# %%
a = 10

# %%
print('\tPython')
print('\t\t\tPython')

# %%
print('C:\path\\to\something\\new')

# %%
print(r'C:\path\to\something\new')

# %%
print('C:\\path\\to\\something\\new')

# %%
import os
os.getcwd()

# %%
print("""
Instrukcja uruchamiania pliku przyklad.py:

    --file [nazwa pliku]
        zapisuje output do pliku
        
    --qiuet
       wycisza logi w konsoli 
Koniec.""")

# %%
text = 'I love Python. '
print(text * 3)
print('how...' * 10)
print('-' * 30)

# %%
'Python'
'Py' 'thon'
print('Py' 'thon')

# %%
url = 'https://test.pl/longlonglonglonglonglonglonglonglonglonglonglonglonglonglonglonglonglong.png'

url2 = ('https://test.pl/longlonglonglonglonglonglonglonglonglonglonglong'
        'longlonglonglonglonglong.png')

# %%
name = 'Python'
print(name + ' 3.9')
print(name, ' 3.9')

# %%
age = 27
imie = 'Klaudiusz'

print(imie + ' ' +str(age))
print(imie,age)
print('{0} ma {1} lat.'.format(imie, age))


# %%
#Zadanie 2

# utworzenie zmiennej
nazwa = 'Python'

# wydrukowanie 'Czesć, Python' do konsoli
print('Cześć, {}'.format(nazwa))

# %%
saldo = 40
saldo += 30
saldo -= 10

print(saldo)

# %%
lokata = 1000
czynnik_akumulacyjny = 1 + 0.04
lokata_po_roku = lokata * czynnik_akumulacyjny
print('Wartosć lokaty po roku:', lokata_po_roku)

# %%
pixel = 150
pixel /= 255
print(pixel)

# %%
base = 2
base  **= 5
print(base)

# %%
x = 103
x %= 10
print(x)

# %%
imie = 'Klaudiusz'
nazwisko = 'Roman'
imie +=  nazwisko
print(imie)

# %%
name = 'Python '
version = '3.7'
name += version
print(name)

# %% Zadanie 3

kwota_poczatkowa = 1000
stopa_procentowa = 5
okres_trwania = 2

fv = kwota_poczatkowa * (1 + stopa_procentowa/100)**2
print(fv)

# %%
















































