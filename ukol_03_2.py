import json

# Nacteni dat ze souboru (zde z "in.json")
with open("body.json", encoding="utf-8") as vstupni_soubor_body:
    body = json.load(vstupni_soubor_body)

# Vypis nactenych dat
#print(body)


import json

with open("bonusy.json","r", encoding="utf-8") as vstupni_soubor_bonusy:
    bonusy = json.load(vstupni_soubor_bonusy)

#print(bonusy)



def mergeDictionary(body, bonusy):
   dict_3 = {**body, **bonusy}
   for key,value in dict_3.items():
       if key in body and key in bonusy:
               dict_3[key] = dict_3[key] + body[key]
   return dict_3
dict_3 = mergeDictionary(body, bonusy)
print(dict_3)

points = mergeDictionary(body, bonusy)

def get_mark(points):
    if points >= 90:
        mark = 1
    elif points >= 70:
        mark = 2
    elif points >= 50:
        mark = 3
    elif points >= 30:
        mark = 4
    else:
        mark = 5
    return mark

znamky = {}
for student, body in dict_3.items():
    znamka = get_mark(body)
    znamky[student] = znamka
print(znamky)

# Ulozeni dat ze slovniku do souboru (zde do "znamky.json")
with open("znamky.json", mode="w", encoding="utf-8") as vystupni_soubor:
    json.dump(znamky, vystupni_soubor, ensure_ascii=False, indent=4)
    




