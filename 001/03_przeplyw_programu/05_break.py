# -*- coding: utf-8 -*-

# %%
for i in '0123456789':
    i = int(i)
    print(i)
    if i == 6:
        print(i)
        break
    
print('Koniec')

# %%
sample = 'Python Course'
for char in sample:
    if char == ' ':
        break
    print(char)
    
print('Koniec')

# %%
for char in 'kowalski@gmail.com':
    if char == '@':
        print('Adres email zweryfikowany.')
        break
else:
    print('Adres email nie jest poprawny')
    
print('Koniec')

# %% Ćwiczenie 8
ps = 'jnhvsoics!vd'
if len(ps) > 10:
    for char in ps:
        if char == '!':
            print('Hasło poprawne')
            break
    else:
        print('Hasło niepoprawne')
else:
    print('Hasło niepoprawne')