print('Exercício de reajuste de preço')
print('***' * 12)


preco = float(input('\nDigite o preço do produto: '))
valor_reajuste = float(input('Digite o valor do reajuste (em %): '))
preco_reajustado = preco + (preco * (valor_reajuste / 100))
print('')
print('***' * 12)


print(f'\nO produto que custava R$ {preco:.2f}, com {valor_reajuste} % de aumento, vai passar a custar R$ {preco_reajustado:.2f}, a partir de agora.')