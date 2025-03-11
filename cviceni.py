#FILIP KOLÁČEK


zvire = input("Zadejte své oblíbené zvíře: ")
#input načte od uživatele data do proměnné
cislo = int(input("Zadejte své oblíbené číslo: "))
#přetypování na číslo

if cislo <= 5:
    print("číslo je menší než 6.")
#jestli je číslo menší nebo rovno 5 tak to vypíše tu větu
elif cislo > 5 and cislo < 20:
    print("číslo je větší než 5 a menší než 20.")
#jestli je číslo větší než 5 a zároveň menší než 20, tak to vypíše větu
else:
    print("číslo je větší než 19.")
#když nesplňuje předchozí podmínky tak to vypíše danou větu

#git příkaz 1 = git add *
#git příkaz 2 = git commit -m "text"
#git příkaz 3 = git push