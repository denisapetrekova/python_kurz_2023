import json
with  open('body.json',encoding='utf-8') as soubor: #načtení dat ze souboru
    body = json.load(soubor)

#print(body)



import json
prospech = {
    "Dušan Kadlec": "Fail",
    "Daniel Svoboda": "Pass",
    "Anežka Benešová": "Fail",
    "Andrea Vaňková": "Fail",
    "Robin Blažek": "Pass",
    "Renáta Tichá": "Pass",
    "Matyáš Vaněk": "Fail",
    "Tereza Procházková": "Fail",
    "Luboš Černý": "Pass",
    "Vasyl Novotný": "Pass",
    "Jaroslav Polák": "Fail",
    "Dušan Kříž": "Pass",
    "Vlasta Kadlecová": "Fail",
    "Zdenka Soukupová": "Pass",
    "Igor Krejčí": "Pass",
    "Stanislav Vaněk": "Pass",
    "Julie Poláková": "Fail",
    "Veronika Fialová": "Fail",
    "Květoslava Dvořáková": "Fail",
    "Ladislav Čermák": "Pass",
    "Dana Marková": "Pass",
    "Miloš Horák": "Pass",
    "Štefan Jelínek": "Fail",
    "Miloš Veselý": "Fail",
    "Aleš Kříž": "Fail",
    "Marcela Machová": "Fail",
    "Blanka Kučerová": "Pass",
    "Šárka Marešová": "Pass",
    "Dalibor Kadlec": "Fail",
    "Robert Pospíšil": "Fail"
}
# Ulozeni dat ze slovniku do souboru (zde do "prospech.json")
with open("prospech.json", mode="w", encoding="utf-8") as vystupni_soubor:
    json.dump(prospech, vystupni_soubor, ensure_ascii=False, indent=4)






