import math 
n = int(input())
coe = input()
rap = input()

bur = [0]*n
dist_coe = [0]*n
dist_rap = [0]*n
ver = 0

coe_c = (float(coe.split()[0]) , float(coe.split()[1]))
rap_c = (float(rap.split()[0]) , float(rap.split()[1]))

for i in range (0,n):
    coord = input()
    bur[i] = (float(coord.split()[0]) , float(coord.split()[1]))
    
for i in range (0,n):
    
    dist_coe[i] = math.sqrt((coe_c[0] - bur[i][0])**2 + (coe_c[1] - bur[i][1])**2)
    dist_rap[i] = math.sqrt((rap_c[0] - bur[i][0])**2 + (rap_c[1] - bur[i][1])**2)
    
    if dist_coe[i] < 1/2*dist_rap[i]:
        print('O coelho pode escapar pelo buraco (%.3f, %.3f).'%(bur[i][0], bur[i][1]))
        ver = ver + 1
        break
    
if ver == 0:
    print('O coelho nao pode escapar.')
 
    



