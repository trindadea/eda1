N = int(input())

for n in range (N):
    pilha = []
    abre = ['(','[','{']
    fecha = [')',']','}']
    duplicata = ['((','[[','{{']
    exp = str(input())
    
    i=0
    dup = False
    
    while i < len(exp):
        if exp[i] in abre:
            if exp[i+1] == exp[i]:
                pilha.append('%s%s' %(exp[i], exp[i+1]))
                i = i + 2
            else:
                pilha.append(exp[i])
                i = i + 1
                
        elif exp[i] in fecha:
            if pilha[-1] in duplicata:
                if exp[i+1] != exp[i]:
                    temp = pilha[-1][0]
                    pilha.pop()
                    pilha.append(temp)
                    
                    i = i + 1
                else:
                    dup = True
                    break
            else:
                pilha.pop()
                i = i + 1
        else:
            i = i + 1
            
    if dup:
        print('A expressão possui duplicata.')
    else:
        print('A expressão não possui duplicata.')