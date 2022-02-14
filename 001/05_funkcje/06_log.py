# -*- coding: utf-8 -*-

import datetime
import time

print(datetime.datetime.utcnow())

def log(message, dt = datetime.datetime.utcnow()):
    print(dt, message)

log('Uruchomienie systemu')

def logi(*args):
    for command in args:
        log(command)
        time.sleep(1)
logi('Uruchomienie systemu', 'Logowanie', 'Restart', 'Wylogowanie')

# %%
#import datetime
     
     
#def log(message, dt=datetime.datetime.utcnow):
#    print(dt(), message)
     
#def logi(*args):
#    for command in args:
#        log(command)
     
#logi('Uruchomienie systemu', 'Logowanie', 'Restart', 'Wylogowanie')    