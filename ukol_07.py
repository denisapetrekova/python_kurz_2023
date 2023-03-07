
class Auto:
    def __init__(self, registracni_znacka, typ_vozidla, najete_km, stav_tachometru, pocet_dni):
        self.registracni_znacka = registracni_znacka
        self.typ_vozidla = typ_vozidla
        self.najete_km = najete_km
        self.dostupne = True #na zacatku je auto vzdy volne
        self.stav_tachometru = stav_tachometru
        self.pocet_dni = pocet_dni
        
    def __str__(self): 
        zakladni_info =  f"{self.registracni_znacka}, {self.typ_vozidla}"
        if self.dostupne:
            return f"{zakladni_info}, potvrzuji zapujceni vozidla"
        else:
            return f"{zakladni_info}, vozidlo není k dispozici."

    def pujc_auto(self):
        self.dostupne = False
    
    def get_info(self):
        return f"{self.registracni_znacka}, {self.typ_vozidla}"
    
    def vrat_auto(self):
        if self.dostupne == True:
            if self.pocet_dni > 7:
                sazba=300
                self.cena =+ (self.pocet_dni * sazba)
                return f"Cena je celkem {self.cena} Kč za {self.pocet_dni} dni."
            elif self.pocet_dni <= 7:
                sazba=400
                self.cena =+ (self.pocet_dni * sazba)
                return f"Cena je celkem {self.cena} Kč za {self.pocet_dni} dni."



auto_1 = Auto("4A2 3020", "Peugeot 403 Cabrio", najete_km=47534, stav_tachometru= 50000, pocet_dni = 5)
auto_1.pujc_auto()
print(auto_1)
print(auto_1.get_info())
print(auto_1.vrat_auto())
auto_2 = Auto("1P3 4747", "Škoda Octavia", najete_km=41253, stav_tachometru= 50000, pocet_dni = 8)
print(auto_2)
print(auto_2.get_info())
print(auto_2.vrat_auto())


znacka = input("Jakou značku preferujete Peugeot nebo Skoda:")
print(znacka)

if znacka == "Peugeot":
    auto_1.pujc_auto()
    print(auto_1)
elif znacka == "Skoda":
    print(auto_2)

    


