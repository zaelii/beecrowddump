
valor = int(input())

lista = []

for i in range(1000):
    acumulo = 0
    while acumulo < valor:
        lista.append(acumulo)
        acumulo = acumulo + 1
    print('N[{0}] = {1}'.format(i,lista[i]))
    