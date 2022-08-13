seg1 = float(input('Primeiro Segmento: '))
seg2 = float(input('Segundo Segmento: '))
seg3 = float(input('Terceiro Segmento: '))

if seg1 < seg2 + seg3 and seg2 < seg1 + seg3 and seg3 < seg1 + seg2: 
    print (f'Os segmentos {seg1}, {seg2}, {seg3}, PODEM FORMAR um triângulo!')
    if seg1 == seg2 == seg3:
        print ('Esse triângulo é EQUILÁTERO!')
    
    elif seg1 != seg2 != seg3 != seg1:
        print ('Esse triângulo é ESCALENO!')
    
    else:
        print ('Esse triângulo é ISÓCELES!')
else: 
    print('Esses segmentos não podem formar um triângulo :(')