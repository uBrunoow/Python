import time
from random import randint

print ('''Suas opções para o jogo: 
[ 0 ] PEDRA
[ 1 ] PAPEL 
[ 2 ] TESOURA''') 
jogada = int(input('Qual é a sua jogada?'))

print ('JO') 
time.sleep(1)
print ('KEN')
time.sleep(1)
print ('PO!!!')

print ('-='*20)

pc = randint(0, 2)

if jogada == 0: 
    print ('Jogador jogou PEDRA')

elif jogada == 1: 
    print ('Jogador jogou PAPEL')

elif jogada == 2: 
    print ('Jogador jogou TESOURA')

else: 
    print ('Joagada INVÁLIDA. Tente novamente')

if pc == 0:
    print ('Computador jogou PEDRA')

elif pc == 1:
    print ('Computador jogou PAPEL')

elif pc == 2:
    print ('Computador jogou TESOURA')


print ('-='*20)

if pc == jogada:
    print('EMPATE')

elif pc == 2 and jogada == 1:
    print ('Computador VENCEU')

elif pc == 0 and jogada == 2:
    print ('Computador VENCEU')

elif pc == 1 and jogada == 0:
    print ('Computador VENCEU')

else:
    print ('Jogador VENCEU')