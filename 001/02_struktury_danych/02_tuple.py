# -*- coding: utf-8 -*-

empty_tuple = tuple()
print(empty_tuple)

# %%
amazon = ('Amazon', 'USA', 'Technology', 1)
print(amazon)
google = ('Google', 'USA', 'Technology', 2)
print(google)

# %%
name = google[0]
print(google[0])
print(name)

# %%
data = (amazon, google)
print(data)

# %%
a = ('Pawel', 'Krakowiak')
print(a)

# %%
imie = 'Pawel'
nazwisko = 'Krakowiak'

# %%
imie, nazwisko, id_user = ('Pawel', 'Krakowiak', '001')

# %%
amazon_name, country,sector, rank = amazon

# %%
stocks = 'Amazon', 'Apple', 'IBM'

print(type(stocks))

# %%
nested = 'Europa', 'Polska', ('Warszawa', 'Kraków', 'Wrocław')
print(nested)

# %%
a = 12
b = 14

c = b
b = a
a = c
print(a, b)

# %%
x, y = 10, 15

x, y = y, x
print(x, y)

# %% Ćwiczenie 2
x = 'Python'
y = 3.7
print((x, y))














