#!/usr/bin/env python
import sys, os, sorters, glob
from sorters import *

dir = sys.argv[1] if len(sys.argv) > 1 else ""

if dir == "":
    dir = input("Który folder chcesz posortować: ")

while not os.path.isdir(dir):
    dir = input(f"Podany folder ({dir}) jest nieprawidłowy, podaj jeszcze raz który folder chcesz posortować: ")

print("Wybierz metodę sortowania: ")
sorters_modules = {}
for i, sorter in enumerate(map(sorters.__dict__.get, sorters.__all__)):
    sorters_modules[str(i + 1)] = sorter
    print(f"{i + 1}. {sorter.show_name}")


sorter = None
while sorter is None:
    chosen = input("Wybór: ")
    sorter = sorters_modules.get(chosen)

files = filter(os.path.isfile, glob.iglob(f"{dir}/**", recursive=True))
new_dir_stucture = sorter.sort(files)
print(f"Nowy układ folderu {dir}")
print(dir)
for dir in new_dir_stucture:
    print(f"\t{dir}/")
    for file in new_dir_stucture[dir]:
        print(f"\t\t{file}")
