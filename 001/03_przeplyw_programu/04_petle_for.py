# -*- coding: utf-8 -*-

# %%
name = 'sas'

for character in name:
    print(character)
    
# %%
name = 'python'
index = 0

for character in name:
    print(index, character)
    index += 1
    
# %%
for index in range(10):
    print(index)
    
# %%
for index in range(len(name)):
    print('Nr indeksu: ',index, 'Litera: ', name[index])
    
# %%
for i in enumerate(name): # tupla (index, znak)
    print(i)
    
for index, character in enumerate(name):
    print('Nr indeksu: ',index, 'Litera: ', character)
    
# %%
for i in [4, 5, 6, 8, 6]:
    print(i)
    
# %%
for i, value in enumerate([4, 5, 6, 8, 6]):
    print(i, value)
    
# %%
for i in range(10, 20):
    print(i)
    
# %%
for i in range(10, 20, 2):
    print(i)

# %%
for i in range(10, -1, -1):
    print(i)
    
# %%
for i in range(10, 100, 10):
    print(i)
    
# %%
techs = 'java'
for i in range(len(techs)):
    print(i, techs[i])
    
# %%
string = 'Python Course'
for char in string[:6]:
    print(char)

# %%
string = 'Python Course'
for char in string[::-1]:
    print(char)
    
# %%
hashtags = '#sport#gym#fitness'
for char in hashtags:
    if char not in '#':
        print(char)

# %%
for char in zip('abcde', '12345'):
    print(char)

# %%
for char, number in zip('abcdef', 'python'):
    print(char, number)
    
# %%
result = ''
hashtags = '#sport#gym#fitness'
for char in hashtags:
    if char not in '#':
        result += char
    else:
        print(result)
        result = ''
print(result)

# %% Ćwiczenie 6
for i in range(21):
    print(i)
    
# %% Ćwiczenie 7
hashtags = '#weekend#good#time#'
temp = ''
for index, char in enumerate(hashtags):
    if char == '#':
        if index != 0:
            print(temp)
        temp = ''
    else:
        temp += char
        
# %%
hashtags = '#weekend#good#time#'
result = ''
for char in hashtags:
    if char not in '#':
        result = result + char
    else:
        if result:
            print(result)
            result = ''        
