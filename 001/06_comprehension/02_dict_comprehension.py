# -*- coding: utf-8 -*-

stocks = {'AMZN.US': 'Amazon.com Inc', 'GOOGL.US': 'Alphabet Inc',
          'AAPL.US': 'Apple Inc', 'UBER.US': 'Uber Technologies Inc',
          'MSFT.US': 'Microsoft Corp'}

# %%
stocks.keys()
stocks.values()
stocks.items()

for key, value in stocks.items():
    print('{:8}: {}'.format(key, value))
    
# %%
stocks_dict = {key:value for (key, value) in stocks.items()}

# %%
stocks_set = {(key, value) for (key, value) in stocks.items()}

# %%
stocks_invert = {value:key for (key, value) in stocks.items()}

# %%
stock_lower_key = {key.lower():value for (key, value) in stocks.items()}

# %%
stock_value_len = {key:len(value) for (key, value) in stocks.items()}

# %%
stock_and_value_len = {key:value + ':' + str(len(value)) for (key, value) in stocks.items()}

# %%
def replace_corp_inc(name):
    name = name.replace('Corp' ,'0')
    name = name.replace('Inc', '1')
    return name

stocks_flag = {k:replace_corp_inc(v) for (k, v) in stocks.items()}

# %%
stocks_corp = {k:v for (k,v) in stocks.items() if 'Corp' in v}
stocks_inc = {k:v for (k,v) in stocks.items() if 'Inc' in v}

# %%
stocks_A = {key:val for (key, val) in stocks.items() if val.startswith('A')}

# %%
stock_A_less_13 = {key:val for (key, val) in stocks.items() \
 if val.startswith('A') if len(val) < 13}
    
# %%
dicts = {'jeden': 1, 'dwa': 2, 'trzy': 3}
print({val:key for (key, val) in dicts.items()})

# %%
stocks_val_type = {key: 'Corp' if 'Corp' in val else 'Inc' for (key, val) in stocks.items()}

# %%
numbers = range(20)
numbers_dict = {}

for number in numbers:
    if number % 2 == 0:
        numbers_dict[number] = number ** 2
print(numbers_dict)

# %%
num_dict_comp = {key: key ** 2 for key in numbers if key % 2 == 0}

# %%
nested_dict = {'001': {'price': 100},
               '002': {'price': 40},
               '003': {'price': 60}}

for key, val in nested_dict.items():
    print(key, val)
    
# %%
{key:val['price'] for (key, val) in nested_dict.items()}

# %%
nested_dict = {'001': {'price': 100, 'items': 4},
               '002': {'price': 40, 'items': 9},
               '003': {'price': 60, 'items': 8}}

# %%
for key, val in nested_dict.items():
    print(key, val)
    
# %%
{key:val['price'] for (key, val) in nested_dict.items()}
{key:val['price'] * val['items'] for (key, val) in nested_dict.items()}

# %%
