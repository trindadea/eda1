str = input()
str_len = len(str)-1
cont = 0

if len(str) % 2 == 0:
    for i in range (0,int(len(str)/2)):
        if str[i] != str[str_len]:
            cont = cont + 1
        str_len = str_len - 1
else:
    for i in range (0,int(len(str)/2 - (1/2))):
        if str[i] != str[str_len]:
            cont = cont + 1
        str_len = str_len - 1
        
if cont == 1 or (cont == 0 and len(str)%2 != 0):
    print('POSSÍVEL')
else:
    print('IMPOSSÍVEL')       
