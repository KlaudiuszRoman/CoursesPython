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

# %%

def funkcja_2(**kwargs):
    for kwarg in kwargs:
        print(kwarg)
        
funkcja_2(**{'a':1, 'b' : 2})
 
# %%
   
def fun(**kwargs):
    print(kwargs)
    
fun(a = 1, b = 4)
fun(x1 = 10, x2 = 20, x3 = 30)

# %%
def fun_2(*args, **kwargs):
    print(args)
    print(kwargs)

fun_2(1, 2, 3, a = 10, b = 12)

# %%
def fun_3(*args, **kwargs):
    print(sum(args))
    print(kwargs.values())

fun_3(1, 2, 3, a = 10, b = 12)

# %% Ćwiczenie 6

def policz_kwargs(*args, **kwargs):
    return len(kwargs)

policz_kwargs(a = 1, b = 2)
policz_kwargs(10, b = 2, c = 3)