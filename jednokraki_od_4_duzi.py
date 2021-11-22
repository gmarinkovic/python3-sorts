# Дата су четири позитивна реална броја који представљају дужине 4 дужи. Напиши програм који испитује да
# ли се од неке 3 од њих може направити једнакокраки троугао.
#
# Улаз: Четири позитивна реална броја (сваки у засебном реду).
#
# Излаз: Једна линија текста у којој пише da ако је могуће направити троугао тј. ne ако није.
#
# Пример 1
# Улаз
# 1.1
# 2.2
# 3.3
# 4.4
# Излаз
# ne
#
# Пример 2
# Улаз
# 3.2
# 2.3
# 3.2
# 4.5
# Излаз
# da
#
# Пример 3
# Улаз
# 3.2
# 2.3
# 1.1
# 1.1
# Излаз
# ne

# provera da li se od tri duzi duzina a, b i c moze napraviti trougao
def moze_trougao(a, b, c):
    return a + b > c and a + c > b and b + c > a

# provera da li se od tri duzi duzina a, b i c moze napraviti jednakokraki trougao
def moze_jednakokraki_trougao(a, b, c):
    return moze_trougao(a, b, c) and (a == b or a == c or b == c)

# ucitavamo duzine duzi
duz1 = float(input("Unesi prvu duz: "))
duz2 = float(input("Unesi drugu duz: "))
duz3 = float(input("Unesi trecu duz: "))
duz4 = float(input("Unesi cetvrtu duz: "))

# proveravamo sve trojke
if moze_jednakokraki_trougao(duz1, duz2, duz3) or \
    moze_jednakokraki_trougao(duz1, duz2, duz4) or \
    moze_jednakokraki_trougao(duz1, duz3, duz4) or \
    moze_jednakokraki_trougao(duz2, duz3, duz4):
    print("da")
else:
    print("ne")
