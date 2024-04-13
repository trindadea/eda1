def men_index(men):
    if men == 'SS':
        return 0
    elif men == 'MS':
        return 1
    elif men == 'MM':
        return 2
    elif men == 'MI':
        return 3
    elif men == 'II':
        return 4
    else:
        return 5

mencoes = [[],[],[],[],[],[]]
index = None

for i in range(int(input())):
    men_aluno = input().split(' ', 1)
    men = men_aluno[0]
    aluno = men_aluno[1]
    
    index = men_index(men)
        
    mencoes[index].append(aluno)
        
    j = 1
    while j < len(mencoes[index]) and mencoes[index][-1-j] > aluno:
        mencoes[index][-j] = mencoes[index][-1-j]
        j = j + 1
    mencoes[index][-j] = aluno

for i in ('SS','MS','MM','MI','II','SR'):
    index = men_index(i)
    for j in range(len(mencoes[index])):
        print(i, mencoes[index][j])