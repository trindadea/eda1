#entradas
data_1 = input()
data_2 = input()
#split e conversão da data inicial em dia e horario inicial
dia_1 = int(data_1.split()[0])
horario_1 = data_1.split()[1]
#split e conversão do horario inicial em horas, minutos e segundos
h_1 = int(horario_1.split(':')[0])
m_1 = int(horario_1.split(':')[1])
s_1 = int(horario_1.split(':')[2])

dia_2 = int(data_2.split()[0])
horario_2 = data_2.split()[1]

h_2 = int(horario_2.split(':')[0])
m_2 = int(horario_2.split(':')[1])
s_2 = int(horario_2.split(':')[2])
#processamento
dias = dia_2 - dia_1
horas = h_2 - h_1
minutos = m_2 - m_1
segundos = s_2 - s_1

if horas < 0:
    dias = dias - 1
    horas = horas + 24
if minutos < 0:
    horas = horas - 1
    minutos = minutos + 60
if segundos < 0:
    minutos = minutos - 1
    segundos = segundos + 60   
#saídas   
if dias < 0 or horas < 0 or minutos <0 or segundos <0:
    print('Data inválida!')
else:
    print (dias, 'dia(s)')
    print (horas, 'hora(s)')
    print (minutos, 'minuto(s)')
    print (segundos, 'segundo(s)')
