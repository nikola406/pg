def je_tah_mozny(figurka, cilova_pozice, obsazene_pozice):
    """
    Ověří, zda se král nebo jezdec může přesunout na danou pozici.
    
    :param figurka: Slovník s klíči 'typ' a 'pozice' (např. {"typ": "král", "pozice": (4, 4)})
    :param cilova_pozice: N-tice (řádek, sloupec)
    :param obsazene_pozice: Množina obsazených pozic
    :return: True, pokud je tah možný, jinak False
    """
    aktualni_pozice = figurka["pozice"]
    typ = figurka["typ"]
    
    # 1. KROK: Je cílová pozice na šachovnici? (řádky i sloupce 1 až 8)
    # Zde student napíše jednoduchou podmínku s and / or
    if not (1 <= cilova_pozice[0] <= 8 and 1 <= cilova_pozice[1] <= 8):
        return False
    
    # 2. KROK: Je cílová pozice volná?
    # Nápověda: operátor 'in' nebo 'not in' pro množiny
    if cilova_pozice in obsazene_pozice:
        return False
    
    # 3. KROK: Pohyb podle typu figury
    if typ == "král":
        # Král se může pohnout maximálně o 1 pole v jakémkoliv směru.
        # Nápověda: rozdíl řádků a sloupců (absolutní hodnota abs()) musí být <= 1.
        return abs(cilova_pozice[0] - aktualni_pozice[0]) <= 1 and abs(cilova_pozice[1] - aktualni_pozice[1]) <= 1
        
    elif typ == "jezdec":
        # Jezdec se pohybuje ve tvaru L (např. rozdíl řádků je 2 a sloupců 1, nebo naopak).
        dr = abs(cilova_pozice[0] - aktualni_pozice[0])
        ds = abs(cilova_pozice[1] - aktualni_pozice[1])
        return (dr == 2 and ds == 1) or (dr == 1 and ds == 2)
        
    return False


if __name__ == "__main__":
    kral = {"typ": "král", "pozice": (4, 4)}
    jezdec = {"typ": "jezdec", "pozice": (3, 3)}
    obsazene_pozice = {(4, 4), (5, 5), (3, 5)}

    # Testy pro krále
    print(je_tah_mozny(kral, (5, 5), obsazene_pozice))  # False (obsazeno)
    print(je_tah_mozny(kral, (5, 4), obsazene_pozice))  # True (o 1 pole dolů)
    print(je_tah_mozny(kral, (6, 6), obsazene_pozice))  # False (příliš daleko - o 2 pole)
    print(je_tah_mozny(kral, (0, 4), obsazene_pozice))  # False (mimo šachovnici)

    # Testy pro jezdce
    print(je_tah_mozny(jezdec, (5, 4), obsazene_pozice))  # True (tvar L: 2 nahoru, 1 doprava)
    print(je_tah_mozny(jezdec, (5, 5), obsazene_pozice))  # False (obsazeno)
    print(je_tah_mozny(jezdec, (4, 6), obsazene_pozice))  # True (tvar L)
    print(je_tah_mozny(jezdec, (10, 3), obsazene_pozice)) # False (mimo šachovnici)