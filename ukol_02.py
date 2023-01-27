## Zadání

#Vyvíjíš software pro obchod s elektronickými součástkami. Firma eviduje informace o počtu součástek na skladě ve slovníku.
#Klíč slovníku je kód součástky a hodnota klíče je počet součástek na skladě.


sklad = {
  "1N4148": 250,
  "BAV21": 54,
  "KC147": 147,
  "2N7002": 97,
  "BC547C": 10
}
#zeptat se na kód součastky
soucastky = input("Zadej kód součástky:")
#mnozstvi = sklad[soucastky]
if soucastky not in sklad:
    print(f"Součástka {soucastky} není skladem.") 

    
if  soucastky in sklad:
    zadane_mnozstvi = int(input("Zadej množství:"))
    if zadane_mnozstvi > sklad[soucastky]:
      print(f"Lze prodat pouze omezené množství {sklad[soucastky]}.")
      sklad.pop(soucastky)

    else:
      print(f"Požadované množství {zadane_mnozstvi}ks je skladem.")
      sklad.pop(soucastky)




#Napiš software, který bude využívat prodavač v případě, že do obchodu přijde zákazník.
#Software se nejprve zeptá na kód součástky a poté na množství, které si zákazník
#chce koupit. Obě informace si ulož. Následně naprogramuj následující varianty:

#* Pokud zadaný kód není ve slovníku, není součástka skladem. Vypiš tedy zprávu, že součástka není skladem.
#* Pokud zadaná součástka na skladě je, ale je jí méně, než požaduje zákazník, vypiš text o tom, že lze prodat pouze omezené množství kusů.
# Následně součástku odeber ze slovníku, protože je vyprodaná.
#* Pokud zadaná součástka na skladě je a je jí dostatek, vypiš informaci, že poptávku lze uspokojit v plné výši, 
# a sniž počet součástek na skladě o množství požadované zákazníkem.

