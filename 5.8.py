n = int(input())
you_died = False

for i in range(n):
    plano_est = sorted(list(input()))
    
    for j in range(3):
        turno = input()
        
        for conteudo in turno:
            if conteudo in plano_est:
                plano_est.remove(conteudo)
            else:
                you_died = True

    if you_died:
        print('You died!')
        you_died = False
    else:
        if plano_est:
            print('Bora ralar:', end = ' ')
            anterior = None
            for conteudo in plano_est:
                if anterior != conteudo:
                    print(conteudo, end = '')
                    anterior = conteudo
                else:
                    continue
            print('')
        else:
            print("It's in the box!")       