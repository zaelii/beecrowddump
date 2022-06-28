valor = float(input())
acumulo = valor
lista = []

lista.append(valor)
for i in range(100):
    acumulo /= 2
    lista.append(acumulo)
    print("N[{}] = {:.4f}".format(i,lista[i]))
