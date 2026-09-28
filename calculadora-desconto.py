print('--- Bem-vindo ao Sistema de Descontos da Loja ---') # solicita ao usuário que insira o valor total da compra, a função float() converte a entrada para um número decimal
valor_compra = float(input('Digite o valor total da compra: R$ ')) 

if valor_compra < 200: #analisa se o valor da compra é menor que 200 reais
    taxa_desconto = 5 #faz a variavel 'taxa_desconto' (desconto) ser 5
elif valor_compra >= 200 and valor_compra < 300: #analisa se o valor da compra é igual ou maior que 200 reais e se o valor é menor que 300 reais
    taxa_desconto = 10 #faz a variavel 'taxa_desconto' (desconto) ser 10
elif valor_compra >= 300: #analisa se o valor da compra é maior que 300 reais
    taxa_desconto = 15 #faz a variavel 'taxa_desconto' (desconto) ser 15
else: # verifica se o valor inserido é válido (algum numero real)
    print('Erro, insira um numero real') #exibe uma mensagem de erro pedindo para o usuario inserir um numero real

valor_desconto = valor_compra * (taxa_desconto / 100) # calcula o valor financeiro do desconto aplicado
valor_final = valor_compra - valor_desconto # calcula o valor final a ser pago subtraindo o desconto

 # Exibe os resultados formatados na tela com 2 casas decimais (.2f)
print('--- Resumo da Compra ---')
print(f'Valor original da compra: R$ {valor_compra:.2f}')
print(f'Desconto aplicado: {taxa_desconto}% (R$ {valor_desconto:.2f})')
print(f'Valor total a pagar: R$ {valor_final:.2f}')
