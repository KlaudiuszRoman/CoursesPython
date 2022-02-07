# -*- coding: utf-8 -*-

text = 'Witaj na kursie Pythona.\nPython jest wspaniały.'

print(text)

# %%
print(dir(text))
print(help(str.count))

# %%
print(text.capitalize()) # pierwsza litera z dużej

# %%
print(text.title()) # każda litera nowego słowa z dużej

# %%
print(text.count('Python')) # ile podciągów wystąpi w tekście

# %%

print(text.startswith('Wi'))

# %%
print('python'.startswith('py'))

# %%
print(text.endswith('y.'))

# %%
print('sample.py'.endswith('.py'))

# %%
print('sample.png'.endswith('.png'))

# %%
print(text.find('Python'))
print(text[text.find('Python'):])

# %%
hashtags = 'sport#gym'
idx = hashtags.find('#')
print(idx)
print(hashtags[:idx])

# %%
print('pa$w7el'.isalnum())

# %%
print('567512'.isdigit())

# %%
print('python'.islower())

# %%
print('PYT'.isupper())

# %%
print(' '.join(['uno', 'dos']))
print('#'.join(['sport', 'gym','fit']))

# %%
print('#good#time#mood'.replace('#', ' '))

# %%
print('column name'.replace(' ', '_'))

# %%
print('        python    '.strip())
print('        python    '.rstrip())
print('        python    '.lstrip())

# %%
print('1,2,3,4,5'.split(','))

print('python java php sql sas'.split())

print('#gym#fit#mood'.split('#'))

# %%
print('12'.zfill(5))
print('1'.zfill(10))

# %% Zadanie 5

print('#'.join(['sport', 'python', 'free', 'time']))

# %% Zadanie 6

x = '123,785,45,5'
print(x.split(','))































