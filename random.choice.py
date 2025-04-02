import random

auta = ["BMW", "Mercedes", "Audi", "Bentley", "Škoda"]

for i in auta:
    print(i)

new = input("Napište značku auta: ")

auta.append(new)

for i in auta:
    print(i)

nahodnaHodnota = random.choice(auta)
print(nahodnaHodnota)
