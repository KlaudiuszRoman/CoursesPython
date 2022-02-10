# -*- coding: utf-8 -*-

# %%
raw_data = '345!23!3234!43434'
result = ''
for raw_data_el in raw_data:
    if raw_data_el == '!':
        print(result)
        result = ''
        continue
    result += raw_data_el
print(result)

# %%
raw_data = '345!23!3234!43434'
clean_data = ''

for char in raw_data:
    if char != '!':
        clean_data += char
    else:
        clean_data += ','
print(clean_data)

# %%
suma = 0
for i in range(10):
    suma += i
print(suma)

# %%
saldo = 450
print('Saldo początkowe: {}'.format(saldo))
for kwota in range(10, 60, 10):
    print('WYpłacono kwota: {}'.format(kwota))
    saldo -= kwota
    print('Saldo: {}'.format(saldo))
    
# %%
pin = input('Podaj PIN: ')
if len(pin) == 4 and pin.isdigit():
    print('PIN zwalidowany!')
else:
    print('Niepoprawna struktura PINu')

# %%
print('Witaj w systemie logownaia.')
print('*' * 30)
nick = input('Podaj swój nick: ')
pin = input('Podaj swój kod PIN, {}: '.format(nick))

if len(pin) == 4:
    for char in pin:
        if char not in '0123456789':
            print('Podałeś niepoprawny kod PIN')
            break
    else:
        print('Kod pin ważny')
else:
    print('Podałeś niepoprawny kod pin.')
    
# %% Ćwiczenie
zones_dict = {'Europe':['Poland', 'Germany'], 'Africa':['RPA','Togo']}
account_dict = {1:{'nick':'Lucjan', 'password':'password1', 'zone':'Europe'}, 
                2:{'nick':'Włodek', 'password':'password2', 'zone':'Africa'}}
print('Witaj w systemie logownaia.')
print('*' * 30)
nick = input('Podaj swój nick: ')
user_id = 0
for find_user_id in account_dict:
    if nick == account_dict[find_user_id]['nick']:
        user_id = find_user_id
        break
else:
    print('Nie ma takiego użytkownika!')
        
if user_id != 0:
    password = input('Podaj swoje hasło, {}: '.format(nick))
    if password != account_dict[user_id]['password']:
        print('Błędne hasło {}! '.format(nick))
    else:
        print('Zalogowano!')
        country = input('Skąd się zalogowałeś: ')
        countru_list_to_get_access = zones_dict[account_dict[user_id]['zone']]
        for country_i in countru_list_to_get_access:
            if country_i == country:
                print('Miłej pracy w systemie!')
                break
        else:
            print('Z tego regionu nie możesz uzyskać dostępu!')