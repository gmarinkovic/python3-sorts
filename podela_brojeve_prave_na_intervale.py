# sortiranje bez nizova 
#
# Бројевна права је трима различитим тачкама a, b и c подељена на четири дела.
# Написати програм који одређује у ком делу, првом, другом, трећем или четвртом,
# се налази унета (четврта) тачка x, различита од тачака a, b и c.
#
# Улаз: На стандарном улазу налазе се 4 различита реална броја, сваки у посебној линији,
# који редом представљају тачке којима је реалне праве подељена (тачке a, b и c)
# и тачку за коју одређујемо у ком делу се налази
# (тачку x).
#
# Излаз: У једној линији стандардног излаза исписује број 1, 2, 3 или 4 у зависности ком делу тачка x припада.
#
# Пример
# Улаз
# 5
# -6
# 3
# 1
# Излаз
# 2
# Funkcija za sortiranje 3 cela broja a, b, c u neopadajucem poretku
# a <= b <= c
def sortiraj3(a, b, c):
    if a > b:
        (a, b) = (b, a)
    if a > c:
        (a, c) = (c, a)
    if b > c:
        (b, c) = (c, b)
    return (a, b, c)

# ucitavamo tri tacke podele
a = float(input("Unesi prvu tacku: "));
b = float(input("Unesi drugu tacku: "));
c = float(input("Unesi trecu tacku: "))

# ucitavamo cetvrtu tacku
x = float(input("Unesi izabranu tacku: "))

# sortiramo tacke podele
(a, b, c) = sortiraj3(a, b, c);

# odredjujemo i ispisujemo interval kome tacka pripada
if x < a:
    print(1)
elif x < b:
    print(2)
elif x < c:
    print(3)
else:
    print(4)
