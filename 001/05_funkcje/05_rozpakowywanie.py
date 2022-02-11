# -*- coding: utf-8 -*-

def test_args(x, *args):
    print('Pierwszy parametr: ', x)
    for arg in args:
        print('Kolejny parametr *args: ', arg)
                
test_args(4, 5, 6, 7, 'a')

# %%
def funkcja_1(x, y, *args):
    print('x=', x)
    print('y=', y)
    print('args=', args)
    
funkcja_1(1, 2)
funkcja_1(1, 2, 3)
funkcja_1(1, 2, 3, 4)

# %%
def suma(x, y):
    return x + y

def suma_dowol(*args):
    return sum(args)

# %%
suma_dowol()

# %% Ćwiczenie 5
def policz_srednia(*args):
    if len(args) == 0:
        print('Brak argumentów do policzenia średniej!')
    else:
        return sum(args) / len(args)
    
policz_srednia(1, 2)