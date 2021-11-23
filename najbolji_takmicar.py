# bez mape
#
# На такмичењу у пливању слободним стилом на 100 метара учествовало је 4 такмичара са старним бројевима
# од 1 до 4. Познати су резултати свих такмичара изражени у секундама. Написати програм који исписује
# стартне бројеве свих оних такмичара који су постигли најбољи резултат (најмање време) на том такмичењу.
#
# Улаз: У четири линије стандардног улаза налазе се четири реална броја из интервала [40, 100], сваки број
# у посебној линији. Бројеви представљају резултате такмичара редом од такмичара са стартним бројем 1 до
# такмичара са стартним бројем 4.
#
# Излаз: На стандардном излазу исписују се стартни бројеви такмичара који су постигли најбољи резултат.
# Сваки стартни број је у посебној линији, старни бројеви су приказани од најмањег до највећег.
#
# Пример
# Улаз
# 54.7
# 50.3
# 50.3
# 58.6
# Излаз
# 2
# 3

# ucitavamo vremena cetiri takmicara
lista1 = [float(input("Unesi rezultat prvog takmicara: ")), float(input("Unesi rezultat drugog takmicara: ")), float(input("Unesi rezultat treceg takmicara: ")), float(input("Unesi rezultat cetvrtog takmicara: "))]

minimal1= min(lista1)
k1=lista1.index(minimal1)
# stampa index ali uvecamo ga za 1 da ni dobili nase redosled koji pocinje od 1 a ne od 0
print(k1+1)

# brisanje minmalnog elementa sa liste
del lista1[k1]

# trazenje novog minimalca
minimal2= min(lista1)
k2=lista1.index(minimal2)

if k2<k1:
    # stampa index ali uvecamo ga za 1 da ni dobili nase redosled koji pocinje od 1 a ne od 0,
    print(k2+1)
else:
    # stampa index ali uvecamo ga za 2 da ni dobili nase redosled koji pocinje od 1 a ne od 0,i za obrisan element
    print(k2+2)
