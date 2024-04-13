n = int(input())
hab = input()
hab = hab.split()

for i in range (n):
    hab[i] = int(hab[i])
hab.sort()
hab.reverse()

titular = 0
reserva = 0

for i in range (11):
    titular = titular + hab[i]
if n <= 22:
    for i in range (11, n):
        reserva = reserva + hab[i]
else:
    for i in range (11, 22):
        reserva = reserva + hab[i]
    
print(titular - reserva)
