#FILIP KOLÁČEK


zvire = input("Zadejte své oblíbené zvíře: ")
#input načte od uživatele data do proměnné
cislo = int(input("Zadejte své oblíbené číslo: "))
#přetypování na číslo

if cislo <= 5:
    print("číslo je menší než 6.")
#jestli splní danou podmínku, tak to vypíše tu větu
elif cislo > 5 and cislo < 20:
    print("číslo je větší než 5 a menší než 20.")
#jestli nesplní první podmínku, ale tuhle druhou ano, tak to vypíše větu
else:
    print("číslo je větší než 19.")
#když nesplňuje předchozí podmínky tak to vypíše danou větu

#git příkaz 1 = git add *
#git příkaz 2 = git commit -m "text"
#git příkaz 3 = git push

#git příkaz 4 = git clone "odkaz"
#git příkaz 5 = cd "daná složka"
#git příkaz 6 = git pull

rok = 2025
text = "Veselé velikonoce"
cislo = 2519846122

#fstring
print (f"Ahoj, {text} {rok}")

#oddělovač tisíců
print (f"{cislo:,}")

#vypsat počet písmen
print (f"{text:.6}")

#desetinná čísla
print (f"{cislo:.3f}")

#převody jednotek
hodnota = 155
print(f"{hodnota:b}")
print(f"{hodnota:x}")