num1 = int(input('Digite um número inteiro: '))
print ('Escolha uma das bases para conversão: ')
print (' [ 1 ] converter para BINÁRIOr \n [ 2 ] converter para OCTAL \n [ 3 ] converter para HEXADECIMAL')
opc = int(input('Sua opção: '))

if opc == 1: 
    print (f'{opc} convertido para BINÁRIO é igual a {bin(num1)[2:]}')

elif opc == 2: 
    print (f'{opc} convertido para OCTAL é igual a {oct(num1)[2:]}')  

elif opc == 3:
    print (f'{opc} convertido para HEXADECIMAL é igual a {hex(num1)[2:]}')

else: 
    print ('Opção inválida. Tente novamente')