n = int(input())
cont = 0
aux = 0

for i in range (n):
    str = input()
    for j in range (1,len(str)-1):
        if str[j] == '0' and str[j-1] == '1':
            index = j
            while str[index] == '0':
                cont = cont + 1
                index = index + 1
                aux = aux + 1
                if index == len(str):
                    cont = cont - aux
                    break
            aux = 0
    print(cont)
    cont = 0
    index = 0
  
    
