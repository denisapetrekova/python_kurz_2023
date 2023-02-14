
def kontrola(telefonni_cislo):
    if len(telefonni_cislo) == 9:
        return True # vse ok
    elif telefonni_cislo[:4] == "+420" and len(telefonni_cislo) == 13:
        return True  # take ok
    else:
        return False  # chybny format


telefonni_cislo = input("Napiš telefonní číslo:") 

if kontrola(telefonni_cislo) == True:
    print(f"Toto telefonní číslo má správný tvar {telefonni_cislo}")
    text_zpravy = input("Napiš text zprávy: ") #pokud je telefonní číslo správné, zeptá se na text zprávy
    print(text_zpravy)
else:
    print(f"Toto telefonní číslo nemá správný tvar {telefonni_cislo}")
    exit() #pokud není telefonní číslo správné, ukončí program

def sms_zprava(text_zpravy):  #funkce k určení ceny za zprávu
    cena = 0
    if len(text_zpravy) <= 180:
        cena = 3
    elif len(text_zpravy) >= 181:
        cena = 6
    else:
        len(text_zpravy) >= 182
        cena = 9
    return cena

text_zpravy = sms_zprava(text_zpravy)
print(f"Cena zprávy je {text_zpravy} Kč.")
