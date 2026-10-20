def je_prvocislo(cislo):
    if cislo < 2:
        return False
    for i in range(2, cislo):
        if cislo % i == 0:
            return False
    return True

def vrat_prvocisla(maximum):
    vysledek = []
    for i in range(1, int(maximum) + 1):
        if je_prvocislo(i):
            vysledek.append(i)
    return vysledek

if __name__ == "__main__":
    vstup = int(input("Zadej maximum: "))
    
    print(f"Je {vstup} prvočíslo?", je_prvocislo(vstup))
    print("Seznam prvočísel:", vrat_prvocisla(vstup))