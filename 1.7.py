import math
total = int(input())
soma_parc = 0
soma = 0
seg_parcial= 0
seg = 0

print ('Transmitindo', total ,'bytes...')

while soma < total:
    bytes = int(input())
    soma_parc = soma_parc + bytes
    soma = soma + bytes
    seg_parcial = seg_parcial + 1
    seg = seg + 1
    
    if seg_parcial == 5:
        if soma_parc == 0:
            print('Tempo restante: pendente...')
        elif soma != total:
            res = math.ceil(round((total - soma)/(soma_parc/5),3))
            print ('Tempo restante:', res, 'segundos.')
        
        seg_parcial = 0
        soma_parc = 0

print('Tempo total:', seg, 'segundos.')
    