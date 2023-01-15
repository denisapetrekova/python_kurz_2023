jmeno = "denisa"
print(f"{jmeno}@czechitas.cz")




jmeno_a_prijmeni = input("Napiš jméno a příjmení:")
#všechna písmena velká
print(jmeno_a_prijmeni.upper())
#všechna písmena malá
print(jmeno_a_prijmeni.lower())
#standartni varianta - prvni písmeno velké a ostatní malé
print(f"{jmeno_a_prijmeni[:1].upper()}{jmeno_a_prijmeni[1:6].lower()} {jmeno_a_prijmeni[7:8].upper()}{jmeno_a_prijmeni[8:].lower()}")
#iniciály
print(f"{jmeno_a_prijmeni[:1].upper()}. {jmeno_a_prijmeni[7:8].upper()}.")
