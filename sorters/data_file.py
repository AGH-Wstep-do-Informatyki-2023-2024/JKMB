import os
import datetime

def data_utworzenia_pliku(nazwa_pliku):
    timestamp = os.path.getctime(nazwa_pliku)
    data_utworzenia = datetime.datetime.fromtimestamp(timestamp)
    return data_utworzenia.strftime('%Y-%m-%d %H:%M:%S')

def miesiac_utworzenia_pliku(nazwa_pliku):
    data_utworzenia = data_utworzenia_pliku(nazwa_pliku)
    data_utworzenia = datetime.datetime.strptime(data_utworzenia, '%Y-%m-%d %H:%M:%S')
    return data_utworzenia.strftime('%B')

folder = '.'  # Aktualny folder - można zmienić na inny folder
pliki = os.listdir(folder)

for plik in pliki:
    if os.path.isfile(plik):
        data = miesiac_utworzenia_pliku(plik)
        print(f'Plik: {plik}, Utworzony w miesiącu: {data}')
