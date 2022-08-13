preco = float(input('Preço das compras: R$'))
print ('Formas de pagamento')
print ('[ 1 ] à vista dinheiro / cheque')
print ('[ 2 ] à vista cartão')
print ('[ 3 ] 2x no cartão')
print ('[ 4 ] 3x ou mais no cartão')

opc = int(input('Qual é a opção? '))

if opc == 1: 
    din = preco - (preco * 0.1)
    print (f'O valor de {preco:.2f} ficará com 10% de desconto R${din:.2f}')

elif opc == 2:
    vst = preco - (preco * 0.05)
    print (f'O valor de R${preco:.2f} ficará com 5% de desconto R${vst:.2f}')

elif opc == 3: 
    crt = preco 
    par = crt / 2
    print (f'O valor de R${preco:.2f} será parcelada em 2x de R${par} ')

elif opc == 4: 
    parcelas =int(input('Quantas parcelas?'))
    juros = preco + (preco * 0.2)
    prcl = juros / parcelas 
    print (f'Sua compra parcelada em {parcelas}x de {prcl:.2f} COM JUROS')
    print (f'Sua compra de R${preco:.2f} vai custar R${juros:.2f}')

else: 
    print ('OPCÃO INVÁLIDA')