entrada_1 = input()
m = int(entrada_1.split()[0])
n = int(entrada_1.split()[1])

entrada_2 = input()
P = entrada_2.split()

lista = []

P = [int(num) for num in P]

i = 0

for i in range (m - n + 1):
    for j in range(i, i+n):
        lista.append(P[j])
    print(sum(lista)//n)
    lista.clear()
