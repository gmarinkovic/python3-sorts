# sa nizovima i primena bibliotecka funkcija
#
# Ученици током године раде 5 контролних задатака. Наставник је обећао да ће приликом закључивања оцена
# сваком ученику занемарити најслабију оцену (ако постоји више таквих, занемариће само једну). Напиши
# програм који учитава 5 оцена једног ученика и исписује просечну оцену када се занемари најслабије урађени
# контролни.
#
# Улаз: У свакој од пет линија стандардног улаза налази се по једна оцена (цео број између 1 и 5) коју је
# ученик добио.
#
# Излаз: Просечна оцена без најлошијег контролног, заокружена на две децимале.
#
# Пример
# Улаз
# 5
# 4
# 4
# 5
# 3
# Излаз
# 4.50

ocene = [ int(input("Prvi: ")), int(input("Drugi: ")), int(input("Treci: ")), int(input("Cetvrti: ")), int(input("Peti: ")) ]

# sortiramo ocene
ocene = sorted(ocene)
del(ocene[0])
print(ocene)
# izračunavamo ocena prosek bez najlošije ocene
# prosek_bez_najlosije = (ocene[1] + ocene[2] + ocene[3] + ocene[4]) / 4

prosek_bez_najlosije = (sum(ocene)) / len(ocene)

# prikaz rezultata
print(format(prosek_bez_najlosije, '.2f'))
