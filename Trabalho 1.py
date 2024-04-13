def crypto(chave):
    tam = len(chave)
    ind_max = tam
    seq = [0]*tam

    algarismos = [1,2,3,4,5,6,7,8,9]
    algarismos = algarismos[:tam]

    for i in range(tam, 0, -1):
        if chave[i-1] == '+':
            seq[i-1] = algarismos.pop()
            for j in range(i, ind_max):
                seq[j] = algarismos.pop()
            ind_max = i-1
    return seq

def deYodafy(instrucao):
    frase = instrucao[:-1].split()
    nova_frase = ''
    
    for i in range(len(frase) - 1):
        nova_frase = nova_frase + frase.pop() + ' '
    return nova_frase + frase.pop() + instrucao[-1]

def merge(intervalos):
    intervalos = intervalos.split()
    
    for i in range (len(intervalos)//2):
        num1 = int(intervalos[i][1:][:-1])
        num2 = int(intervalos[i+1][:-1])
        intervalos[i] = [num1, num2]
        del intervalos[i+1]

    intervalos.sort()

    i = 0
    while i < len(intervalos) - 1:
        if intervalos[i][1] >= intervalos[i+1][0]:
            if intervalos[i][1] >= intervalos[i+1][1]:
                del intervalos[i+1]
            else:
                intervalos[i][1] = intervalos[i+1][1]
                del intervalos[i+1]
        else:
            i = i + 1
    return intervalos

#Entradas e processamentos de dados

solicitacoes = []
bloco_processos = 0

while True:
    comando = input()
    if comando == 'halt':
        break
    
    elif comando.split()[0] == 'add': #o comando 'add' adiciona uma solicitação de comandos especiais na fila 'solicitacoes'
        solicitacoes.append([])
        bloco_processos = len(solicitacoes) #o bloco de processos garante que os comandos especiais serão adicionados em suas devidas solicitações
        for i in range(int(comando.split()[1])):
            comando_esp = input()
            comando_esp = comando_esp.split(' ', 1)
            solicitacoes[bloco_processos - 1].append((comando_esp[0], comando_esp[1]))  
        
    elif comando == 'process' and solicitacoes:
        comando_atual = solicitacoes[0][0]
        if comando_atual[0] == 'crypto':
            seq = crypto('+' + comando_atual[1]) #o argumento da função 'crypto' é somado com o caractere '+' para facilitar o processamento
            print(*seq, sep = '')
        elif comando_atual[0] == 'deYodafy':
            nova_frase = deYodafy(comando_atual[1])
            print(nova_frase)
        else:
            intervalos = merge(comando_atual[1])
            print(*intervalos, sep = ' ')
            
        solicitacoes.append(solicitacoes.pop(0)[1:]) #seguindo a execução do comando 'process', o bloco de processos é movido para o fim da fila de acordo com a abordagem round-robin
        if not solicitacoes[-1]:
            del solicitacoes[-1]

com_orf = 0
for solicitacao in solicitacoes:
    com_orf = com_orf + len(solicitacao)
print('%i processo(s) e %i comando(s) órfão(s).' %(len(solicitacoes), com_orf))