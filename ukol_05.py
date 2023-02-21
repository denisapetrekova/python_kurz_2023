teploty = [
    [2.1, 5.2, 6.1, -0.1],
    [2.2, 4.8, 5.6, -1.0],
    [3.3, 6.5, 5.9, 1.2],
    [2.9, 5.6, 6.0, 0.0],
    [2.0, 4.6, 5.5, -1.2],
    [1.0, 3.2, 2.1, -2.0],
    [0.4, 2.7, 1.3, -2.8]
]

    #Vytvořte seznam průměrných teplot pro každý den.
teplota_prumer_den = [round(sum(cislo[:3])/len(cislo[:3])) for cislo in teploty]
   
    #print(teplota_prumer_den)
    #Vytvořte seznam ranních teplot.
teplota_rano = [cislo[0] for cislo in teploty]
  
    #print(teplota_rano)
    #Vytvořte seznam nočních teplot.
teplota_nocni = [cislo[3] for cislo in teploty]
    #print(teplota_nocni)
    #Vytvořte seznam dvouprvkových seznamů obsahujících pouze polední a noční teplotu.
teploty_dve = [(cislo[1],cislo[-1]) for cislo in teploty]
