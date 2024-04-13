alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def decompress(n):
    if n == 0:
        return ''    
    i = n%(2**5)
    return alfabeto[i-1] + decompress(n//(2**5))
#AAAAA ENTENDI