
v = int(input())
acumulo = 0
lista = []

print("N[{}] = {}".format(0,v))
for i in range(9):
    acumulo = v*2
    v = acumulo
    lista.append(acumulo) 
    print("N[{}] = {}".format(i+1,acumulo))
    
    
