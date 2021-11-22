# Од цифара четвороцифреног природнog броја треба формирати најмањи троцифрен број.
#
# Улаз: У првој линији стандардног улаза налази се четвороцифрен природан број n (1000 ≤ n < 10000).
#
# Излаз: Најмањи троцифрен број добијен од цифара броја n.
#
# Пример
# Улаз
# 5302
# Излаз
# 203

# funkcija za uredjivanje 4 cela broja a, b, c, d
# u neopadajuci poredak a <= b <= c <= d
def sortiraj4(a, b, c, d):
    if a > b:
        (a, b) = (b, a)
    if a > c:
        (a, c) = (c, a)
    if a > d:
        (a, d) = (d, a)
    if b > c:
        (b, c) = (c, b)
    if b > d:
        (b, d) = (d, b)
    if c > d:
        (c, d) = (d, c)
    return (a, b, c, d)

# funkcija za kreiranje trocifrenog broja abc
def trocifreni_broj(a, b, c):
    return 100 * a + 10 * b + c

# citanje broja
broj = int(input("Unesi broj: "))

# odredjivanje cifra broja /razvrstavanje
c0 = broj % 10
c1 = broj // 10 % 10
c2 = broj // 100 % 10
c3 = broj // 1000

# uredjivanje cifara tako da je c0 <= c1 <= c2 <= c3
(c0, c1, c2, c3) = sortiraj4(c0, c1, c2, c3);
# formiranje i ispis najmanjeg trocifrenog broja
# izbacujemo c3 kao najveci jer trazimo najmanji
if c0 != 0:
    x = trocifreni_broj(c0, c1, c2)
elif c1 != 0:
    x = trocifreni_broj(c1, c0, c2)
elif c2 != 0:
    x = trocifreni_broj(c2, c0, c1)
else:
# ako su c0,c1,c2 jednaki nuli onda ukljucujemo c3
    x = trocifreni_broj(c3, c0, c1)

print("Najmanji trocifreni broj je: "+str(x))
