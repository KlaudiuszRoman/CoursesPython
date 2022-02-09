# -*- coding: utf-8 -*-

# %%
techs = []
print(techs)

# %%
techs.append('python')
print(techs)

# %%
techs.append('java')

# %%
techs.append(['hadoop', 'spark'])
print(techs)

# %%
techs.extend(['sql', 'sas'])
print(techs)

# %%
techs.insert(0, 'go')
print(techs)

# %%
techs.insert(2, 'r')
print(techs)

# %%
print(techs)
print(techs.pop())
print(techs)

# %%
# techs = ['python', 'java', 'sql', 'php']
print(techs.pop(0))
print(techs)

# %%
techs = ['python', 'java', 'sql', 'php']

techs.index('java')
techs.idnex('j')

# %%
techs = ['python', 'java', 'sql', 'php', 'python']
techs.count('python')
techs.count('pyth')

# %%
techs = ['python', 'java', 'sql', 'php', 'r', 'angular']
techs.sort(reverse = True)
print(techs)

# %%

techs = ['python', 'java', 'sql', 'php', 'r', 'angular']
techs[::]
techs.reverse()
print(techs)

# %%
techs[1] = 'c++'
print(techs)

# %% Ćwiczenie 5
l1 = [4, 5, 3, 3]
l2 = [9, 7]
l1.extend(l2)
print(l1)

# %% Ćwiczenie 6
l1 = ['Apple', 'Microsoft', 'Samsung', 'Netflix', 'Uber']
l1.append('Amazon')
l1.append('Google')
print(l1)