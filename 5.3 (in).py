n = int(input())
lista = input().split()
pecas_dup = 0

while lista:
    peca = lista.pop()
    while peca in lista:
        lista.remove(peca)
        pecas_dup = pecas_dup + 1
print(pecas_dup)