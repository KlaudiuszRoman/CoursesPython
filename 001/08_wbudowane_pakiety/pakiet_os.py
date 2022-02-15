# -*- coding: utf-8 -*-

import os

# %%
dir(os)

# %%
os.getcwd()

# %%
os.chdir('..')

# %%
os.getcwd()

# %%
os.system('mkdir dir1 dir2 dir3')

# %%
os.rmdir('dir1')

# %%
os.listdir()

# %%
for item in os.listdir():
    print(item)
    
# %%
for item in os.listdir():
    if item.endswith('.py'):
        print(item)
        
# %%
for root, dirs, files in os.walk(os.getcwd()):
    print(root)
    print(dirs)
    print(files)
    
# %%
os.path.join(r'home\user\bin', 'python')