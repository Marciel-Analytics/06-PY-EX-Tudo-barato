# variáveis
total_da_compra = 0
cont_mais_de_1000 = 0
menor_preco = cont = 0
nome_do_barato = ' '

print('-'*60)
print('--- LOJA TUDO BARATÂO ---')
print('-'*60)

while True:
    nome_produto = str(input('QUAL O NOME DO PRODUTO: '))
    preco_produto = float(input('QUAL O PREÇO DO PRODUTO: '))
    cont += 1
    total_da_compra += preco_produto

    if preco_produto > 1000:
        cont_mais_de_1000 += 1

    if cont == 1:
        menor_preco = preco_produto
        nome_do_barato = nome_produto
    else:
        if preco_produto < menor_preco:
            menor_preco = preco_produto
            nome_do_barato = nome_produto

    print('-' * 60)
    avancar = ' '
    while avancar not in 'SN':
        avancar = str(input('QUER CONTINUAR [S/N]: ')).strip().upper()[0]
        print('-' * 60)

    if avancar == 'N':
        break

print('-'*60)
print(f'O TOTAL DA COMPRA FOI DE: {total_da_compra}')
print(f'QUANTOS PRODUTOS CUSTAM MAIS DE 1000,OO R$: {cont_mais_de_1000}')
print(f'QUAL O NOME DO PRODUTO MAIS BARATO: {nome_do_barato}')