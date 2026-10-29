import sys
import re

def inkrementuj_cisla(data):
    for radek in data:
        rozdeleny = radek.split(",")
        for prvek in rozdeleny:
            print(prvek)
    return data

def nacti_radky(file_name):
    radky = []
    with open(file_name, "r") as file:
        for line in file:
            radky.append(line.strip())
    return radky

def zapis_radky(file_name, data):
    with open(file_name, "w") as file:
        for line in data:
            file.write(line + "\n")

if __name__ == "__main__":

    if len(sys.argv) <= 1:
        print(f'Pouziti: python {sys.argv[0]} jmeno_souboru')
        sys.exit()

    file_name = "data.txt"  # data.txt

    try:
        data = nacti_radky(file_name)
    except FileNotFoundError:
        print(f'Soubor {file_name} neexistuje')
        
    data = inkrementuj_cisla(data)

    name = file_name.split('.')  #  name = ['data', 'csv']

    file_name2 = name[0] + '2.' + name[1]  #  'data2.txt'
    zapis_radky(file_name2, data)



