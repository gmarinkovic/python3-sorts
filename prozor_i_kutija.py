# Петар и Лука треба да изнесу кутију облика квадра датих димензија a, b, c, кроз прозор облика правоугаоника
# димензија p × q тако да су одговарајуће ивице кутије буду паралелне ивицама прозора. Написати програм
# којим се проверава да ли је то могуће.
#
# Улаз: Са стандардног улаза уносе се 5 природних бројева који представљају редом димензије кутије a, b, c и
# прозора p, q изражене у центиметрима.
#
# Излаз: У једној линији стандардног излаза приказати реч da ако је могуће кутију изнети кроз прозор, а реч
# ne ако то није могуће.
#
# Пример 1
# Улаз
# 75
# 30
# 50
# 70
# 60
# Излаз
# da
#
# Пример 2
# Улаз
# 30
# 40
# 50
# 30
# 40
# Излаз
# da

# ucitavamo i sortiramo dimenzije kutije
print("Dimenizije kutije: ")
a = [int(input("Prva dimenzija: ")), int(input("Drugi dimenzija: ")), int(input("Treca dimenzija: "))]
a = sorted(a)
# ucitavamo i sortiramo dimenzije prozora

print("Dimenizje kutije: ")
p = [int(input("Prva dimenzija: ")), int(input("Druga dimenzija: "))]
p = sorted(p)

# proveravamo da li kutija moze da prodje (optimalno okrenuta)
if a[0] <= p[0] and a[1] <= p[1]:
    print("da")
else:
    print("ne")
