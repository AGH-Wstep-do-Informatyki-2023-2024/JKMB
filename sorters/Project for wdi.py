import os, shutil

path =  str(input("Podaj ścieżkę folderu aby posortować w nim pliki: "))
list = [a, ą, e, ę, i, o, u, y]
separate = os.listdir(path)
f_name = ["Samogłoski, spółgłoski"]
for x in len(f_name):
    if not os.path.exists(path+folder_name[x]):
        os.makedirs(path+folder_name[x])
for i in len(list):
    r = separate[i][-1].lower()
    if r[0] == list:
        shutil.move(path+files, path+'Samogłoski'+files)
    else:
        shutil.move(path+files, path+'Spółgłoski'+files)





