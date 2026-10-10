def cislo_text(cislo):
    # funkce zkonvertuje cislo do jeho textove reprezentace
    # napr: "25" -> "dvacet pět", omezte se na cisla od 0 do 100
    hodnota = int(cislo)
    jednotky = ["nula", "jedna", "dva", "tři", "čtyři", "pět", "šest", "sedm", "osm", "devět", "deset"]
    desitky = ["", "", "dvacet", "třicet", "čtyřicet", "padesát", "šedesát", "sedmdesát", "osmdesát", "devadesát"]

    if hodnota == 100:
        return "sto"

    if hodnota < 20:
        return jednotky[hodnota]
    
    desitka = hodnota // 10
    jednotka = hodnota % 10

    if jednotka == 0:
        return desitky[desitka]
    else:
        return f"{desitky[desitka]} {jednotky[jednotka]}"


if __name__ == "__main__":
    cislo = input("Zadej číslo: ")
    text = cislo_text(cislo)
    print(text)