# Obsah
  - [Logo](#Logo)
  - [Úkol](#Úkol)
    - [Kód-1](#Kód-1)
    - [Kód-2](#Kód-2)
# Logo

![OIP (1)](https://github.com/user-attachments/assets/6d570aec-04b0-4ee1-9173-18057dddc5ff)

# Úkol
Zde je kód úkolu.
## Kód-1
Uživatele se to zeptá na jméno a věk a poté to vypíše danou větu.
```python
jmeno = input("Jak se jmenujete? ")
vek = int(input("kolik je vám let? "))

print(f"Ahoj, jmenuji se {jmeno} a je mi {vek} let.")
```

## Kód-2
Uživatele se to zeptá na dvě desetinná čísla a pak to s nimi dělá matematické operace
```python
cislo1 = float(input("Zadejte první desetinné číslo: "))
cislo2 = float(input("Zadejte druhé desetinné číslo: "))

soucet = cislo1+cislo2
rozdil = cislo1-cislo2
soucin = cislo1*cislo2
podil = cislo1/cislo2

print (f"Součet vašich čísel je {soucet:.2f}")
print (f"Rozdíl vašich čísel je {rozdil:.2f}")
print (f"Součin vašich čísel je {soucin:.2f}")
print (f"Podíl vašich čísel je {podil:.2f}")
```
