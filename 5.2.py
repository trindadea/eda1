n = int(input())
tabela = []

for i in range(n):
    tabela.append([input()])
    tabela[i].append(round(sum(map(float, input().split())), 3))
    
    atual = tabela[i]
    j = i
    
    while j > 0 and atual[1] < tabela[j-1][1]:
        tabela[j] = tabela[j-1]
        j = j-1
        
    tabela[j] = atual
    
for i in range(n):
    tempo = tabela[i][1]
    mins = int(tempo/60)
    segs = tempo - (mins*60)
    
    print('%i. %s (%i:%06.3f)' %(i+1, tabela[i][0], mins, segs))