def bin_to_dec(binarni_cislo):
    # funkce spocita hodnotu predavaneho binarniho cisla (binarni_cislo muze byt str i int!!!)
    # 111 -> 7
    # "101" -> 5
    cislo = str(binarni_cislo)  # int i str prevedeme na retezec
    vysledek = 0
    for cislice in cislo:
        if cislice not in "01":
            raise ValueError(f"'{cislo}' neni binarni cislo")
        vysledek = vysledek * 2 + int(cislice)
    return vysledek


def test_bin_to_dec():
    assert bin_to_dec("0") == 0
    assert bin_to_dec(1) == 1
    assert bin_to_dec("100") == 4
    assert bin_to_dec(101) == 5
    assert bin_to_dec("010101") == 21
    assert bin_to_dec(10000000) == 128


if __name__ == "__main__":
    test_bin_to_dec()
    print(bin_to_dec(10011101))
    print(bin_to_dec("10011101"))