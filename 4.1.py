entrada = input()
Q1 = int(entrada.split()[0])
Q2 = int(entrada.split()[1])
div = min(Q1,Q2)

while div >= 1:
    
    if Q1%div == 0 and Q2%div == 0:
        print(div)
        break
    else:
        div = div - 1