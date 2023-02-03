preco = float(input('Preço das compras: R$ '))
print('FORMAS DE PAGAMENTO\n'
      '\n[1] à vista dinheiro/cheque'
      '\n[2] à vista cartão'
      '\n[3] 2x no cartão'
      '\n[4] 3x ou mais no cartão')

opcao = int(input('Qual é a opção? '))

if opcao == 1:
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(preco, (preco - (preco*10/100))))
elif opcao == 2:
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(preco, (preco - (preco*5/100))))
elif opcao == 3:
    print('Sua compra vai custar o valor normal de R${:.2f}'.format(preco))
elif opcao == 4:
    parcela = int(input('Quantas parcelas? '))
    juros = preco + (preco*20/100)
    print('Sua compra será parcelada em {}x de {:.2f} COM JUROS'.format(parcela, (juros/parcela)))
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(preco, juros))



