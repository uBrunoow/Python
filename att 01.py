import math
import time

print ('-=          Bem-Vindo ao menu          =-')
time.sleep(2)
print ('Suas escolhas: ')
time.sleep(1)
print ('[ 1 ] Função para retornar o menor valor.')
time.sleep(1)
print ('[ 2 ] Função para ver a distância entre dois pontos.')
time.sleep(1)
print ('[ 3 ] Função de potência.')
time.sleep(3)
r = int(input('Escolha: '))

print('PENSANDO...')

time.sleep(5)
if r == 1:
    print ('-='*9)
    print ('FUNÇÃO DO MENOR VALOR')
    print ('-='*9)
    a = int(input('Digite o numero A: '))
    b = int(input('Digite o numero B: '))

    if a < b:
        print(f'O menor valor entre {a} e {b} é A. Ou seja {a}')

    else:
        print(f'O menor valor entre {a} e {b} é B. Ou seja {b}')

elif r == 2:
    time.sleep(5)
    print ('-='*9)
    print ('FUNÇÃO DA DISTÂNCIA ENTRE DOIS PONTOS')
    print ('-='*9)
    a = int(input('Digite a coordenada X do ponto A: '))
    b = int(input('Digite a coordenada Y do ponto A: '))
    c = int(input('Digite a coordenada X do ponto B: '))
    d = int(input('Digite a coordenada Y do ponto B: '))

    dab = math.sqrt(math.pow(c - a, 2) + math.pow(d - b, 2))
    print (f'O resultado da distancia entre o ponto A e o ponto B é igual a: {dab}')

elif r == 3:
    time.sleep(5)
    print ('-='*9)
    print ('FUNÇÃO DE POTÊNCIA')
    print ('-='*9)

    b = int(input('Digite a BASE: '))
    e = int(input('Digite o EXPOENTE: '))

    x = math.pow(b , e)
    print (f'O reultado da sua potência é {x}')

else: 
    print('Essa não é uma opção. Retorne ao menu >.<')