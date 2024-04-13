def sabacchard(cartas, escolhe):
    if len(cartas) > 1:
        if escolhe:
            c_esq = cartas[0]
            c_dir = cartas[-1]
            if (str(cartas)[1:-1]) in escolhas:
                return escolhas.get((str(cartas)[1:-1]))
            else:
                soma =  max(
                    c_esq + sabacchard(cartas[1:], False),
                    c_dir + sabacchard(cartas[:-1], False))
                escolhas[str(cartas)[1:-1]] = soma
                return soma
        else:
            return max(
                sabacchard(cartas[1:], True),
                sabacchard(cartas[:-1], True))
    else:
        return 0
    
n = input()
cartas = list(map(int, input().split()))
escolhas = {}
    
print(sabacchard(cartas, True))