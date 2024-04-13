import timeit

def len01(palavra):
    resposta = 0
    for _ in palavra:
        resposta += 1
    return

t1 = timeit.Timer('len01("a"*100000)', "from __main__ import len01")
print("len01",t1.timeit(number=1000), "milissegundos")

t2 = timeit.Timer('len02("a"*100000)', "from __main__ import len02")
print("len02",t2.timeit(number=1000), "milissegundos")


