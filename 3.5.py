from Deque import Deque

nomes = input()
nomes = nomes.split()
fila = Deque()

for i in range (len(nomes)):
    fila.addFront(nomes[i])
    
trocas = int(input())

i = 0

while i != trocas:
    fila.addFront(fila.removeRear())
    i = i + 1
    
print('Pessoa da frente: ', fila.removeRear())
print('Pessoa do fim: ', fila.removeFront())