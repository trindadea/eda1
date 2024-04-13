entrada = None
item = None
preco = None
lista=[]
fim = False

while not fim:
    entrada = input()
    if entrada == 'fim':
        fim = True
        break
    
    item = entrada.split()[0]
    preco = entrada.split()[1]
        
    if item == '-':
        for i in range(len(lista)):
            if lista[i][1] == preco:
                del lista[i]
                break
                
    else:
        preco = float(preco)
        lista.append((preco, item))

lista.sort()
lista.reverse()
preco = 0

for i in range (len(lista)):
    print("%s: R$ %.2f" %(lista[i][1], lista[i][0]))
    preco = preco + lista[i][0]

print("----------------------")
print("%i item(ns): R$ %.2f" %(len(lista), preco))