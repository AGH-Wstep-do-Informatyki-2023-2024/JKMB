import os, shutil
from jkmb import dir

path =  str(input("Podaj ścieżkę folderu aby posortować w nim pliki: "))
list = ["a", "ą", "e", "ę", "i", "o", "u", "y"]
separate = os.listdir(path)
f_name = ["Samogłoski, spółgłoski"]
for x in len(f_name):
    if not os.path.exists(path+dir[x]):
        os.makedirs(path+dir[x])
for i in len(list):
    r = separate[i][-1].lower()
    if r[0] == list:
        shutil.move(path+dir, path+'Samogłoski'+dir)
    else:
        shutil.move(path+dir, path+'Spółgłoski'+dir)
