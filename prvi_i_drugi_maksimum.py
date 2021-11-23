# Написати програм којим се одређују највећа два различита броја од пет датих целих бројева.
#
# Улаз: На станадардном улазу налазе се 5 целих бројева, сваки у посебној линији.
#
# Излаз: Прва линија стандарног излаза садржи највећи број од датих 5 бројева. Друга линија стандардног
# излаза садржи други по величини цео број од датих 5 бројева. Aко су сви унети бројеви једнаки друга линија
# треба да садржи само знак ‘-’.
#
# Пример 1
# Улаз
# 2
# 7
# -4
# 7
# 3
# Излаз
# 7
# 3
#
# Пример 2
# Улаз
# 12
# 12
# 12
# 12
# 12
# Излаз
# 12
# -

lista = [int(input("Uneti prvi broj: ")), int(input("Uneti drugi broj: ")), int(input("Uneti treci broj: ")),int(input("Uneti cetvrti broj: ")),int(input("Uneti peti broj: "))]

# sortianje
lista =sorted(lista)

# obrnuti redosled
lista.reverse()

max1=lista[0]
k=1
for i in range (1,len(lista)-1):
    if lista[i]<max1:
        max2=lista[i]
        break
    else:
        k=k+1

if k==len(lista)-1:
    max2="-"

print("Maksimum je: "+str(max1))
print("Prvi posle maksimuma je: "+str(max2))
