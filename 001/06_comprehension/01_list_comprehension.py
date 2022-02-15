# -*- coding: utf-8 -*-

results = []
for i in range(100):
    results.append(i ** 2)
print(results)

# %%
results_2 = [i ** 2 for i in range(100)]
print(results_2)

# %%
lista = [i * 3 for i in range(100)]

# %%
results = []
for i in range(100):
    if i % 5 == 0:
        results.append(i ** 2)
        
# %%
results_2 = [i ** 2 for i in range(100) if i % 5 == 0]

# %%
letters = ['a', 'b', 'c']
numbers = [1, 2, 3]

results = []
for letter in letters:
    for number in numbers:
        results.append(letter + str(number))
        
# %%
results_2 = [letter + str(number) for letter in letters for number in numbers]

# %%
letters_1 = ['a', 'b', 'c']
letters_2 = ['a', 'b', 'c']

results = [letter_1 + letter_2 for letter_1 in letters_1 \
           for letter_2 in letters_2 if letter_1 != letter_2]
    
# %%
[[j for j in range(10)] for i in range(10)]

# %%
[[(i, j) for j in range(10)] for i in range(3)]

# %%
[[i * j for j in range(10)] for i in range(3)]

# %%
[[l1 + l2 for l2 in 'abcde'] for l1 in '12345']

# %%
def silnia(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * silnia(n - 1)
    
[silnia(i) for i in range(5)]

# %% Ćwiczenie 1

print([i for i in range(31) if i % 4 == 0])