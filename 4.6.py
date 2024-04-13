res = []
def quadper(n):
    if n == 0:
        global soma
        soma = sum(res)
        return
    ele = 2*n - 1
    res.insert(0, ele)
    quadper(n-1)
        
    if len(res) > 1:
        print('%i + soma(%s)' %(res.pop(0), res))
    else:
        print('%i' %res[0])

n = int(input())
quadper(n)

print('---------------\n%i ** 2 == %i' %(n, soma))