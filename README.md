# 🏷️ Sistema de Desconto

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)
![Desconto](https://img.shields.io/badge/Desconto-ff69b4?style=for-the-badge)

## 🎯 Objetivo do Sistema
Um programa de linha de comando desenvolvido para calcular e aplicar descontos automaticamente no valor total de uma compra em uma loja online, dependendo da faixa de preço atingida pelo cliente.

## 💻 Linguagem Utilizada
- **Python 3**

## 🧮 Como o cálculo é feito?
O sistema utiliza a estrutura de decisão (`if/elif/else`) para definir a porcentagem de desconto baseada no valor da compra:
- **Menor que R$ 200,00:** 5% de desconto
- **De R$ 200,00 até R$ 299,99:** 10% de desconto
- **A partir de R$ 300,00:** 15% de desconto

Após definir a taxa, as seguintes fórmulas são aplicadas:
`valor_desconto = valor_compra * (taxa_desconto / 100)`
`valor_final = valor_compra - valor_desconto`

## 🚀 Como executar o programa
1. Certifique-se de ter o Python instalado na máquina.
2. Abra o terminal na pasta do projeto.
3. Execute o comando:
   ```bash
   python calculadora-desconto.py
