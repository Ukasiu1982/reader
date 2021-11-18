import os
import sys
import csv

file_input = sys.argv[1]
file_output = sys.argv[2]
changes = sys.argv[3:]

def obsluga_CSV():
    if not os.path.isdir(file_output):
        print(f'błąd podanej ścieżki {file_output} lub podany katalog nie istnieje ')
        os.makedirs(file_output)
        print('katalog został utworzony')

    wyzszy_katalog, nazwa_pliku = os.path.split(file_input)
    if not os.path.isfile(file_input):
        print(f'błąd nazwy {nazwa_pliku} lub podany plik nie istnieje ')
        print(f"Pliki w katalogu {wyzszy_katalog}:")
        print(os.listdir(wyzszy_katalog))
    else:
        with open(file_input, 'r') as plik:
            reader = csv.reader(plik, skipinitialspace=True)
            file_data = []
            for wiersz in reader:
                file_data.append(wiersz)
        for zmiana in changes:
            z = zmiana.split(',')
            liczba_wierszy = len(file_data)
            liczba_kolumn = len(file_data[0])

            if liczba_wierszy > int(z[0]) and liczba_kolumn > int(z[1]):
                file_data[int(z[0])][int(z[1])]=z[2]

    sciezka_nowego_pliku = os.path.join(file_output, nazwa_pliku)
    with open(sciezka_nowego_pliku, 'w') as save_file:
        writer = csv.writer(save_file)
        for linia in file_data:
            writer.writerow(linia)

obsluga_CSV()

# python main.py "katalog1/katalog11/katalog111/hurricanes.csv" "katalog1/katalog11/katalog200" "6,6, 666" "7,6, 777"


