L = int(input())

lista = [0]*L
classe_1 = [0]
classe_2 = [0]
classe_3 = [0]

for i in range (L):
    lista[i] = int(input())

for i in range (L):
    if lista[i] < 10:
        classe_1.append(lista[i])
    elif lista[i] >= 10 and lista[i] < 20:
        classe_2.append(lista[i])
    else:
        classe_3.append(lista[i])

classe_1.sort()
classe_2.sort()
classe_3.sort()

print (classe_1.pop(), classe_2.pop(), classe_3.pop())
