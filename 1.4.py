def primos_gemeos(n):
    pares = 0
    i = 3
    cont = 0
    primos=[2]
    gemeos=[]

    
    while pares != n:
        for j in range (i,1,-1):
            if i%j == 0:
                cont = cont + 1
        
        if cont == 1:
            primos.append(i)
            
            if primos[len(primos)-1] == primos[len(primos)-2] + 2:
                gemeos.append(((primos[len(primos)-2], primos[len(primos)-1])))
                pares = pares + 1
        
        cont = 0
        i = i + 1
    
    return gemeos
        
       
    
       
        
      
    
        
    
      