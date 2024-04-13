from Queue import Queue

entrada = input()
saida = []
enq = Queue()

for char in entrada:
    if char != '*':
        enq.enqueue(char)

for char in entrada:
    if char == '*':
        saida.append(enq.dequeue())

saida = ''.join(saida)
print(saida)