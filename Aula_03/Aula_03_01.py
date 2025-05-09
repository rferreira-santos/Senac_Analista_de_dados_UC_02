#1 – O Ministro da Saúde, entrou em contato com você e te solicitou um auxílio, para obter as seguintes informações sobre os dados da vacinação da covid nos últimos quatro anos:
#- O total e a média de pessoas vacinadas no período.
#- O total e a média da população do Brasil.
#- A taxa de vacinação anual, dos últimos 4 anos, sabendo que para se chegar a esse número, deve-se dividir a quantidade de vacinados pela quantidade da população.
#Ele te enviou os seguintes dados:
#● População Vacinada: 30000000, 25000000, 10000000, 5000000
#● População Total: 213317639, 214477744, 215574303, 216687971
#E pediu para apresentar na tela o resultado das informações solicitada

#Importando a Biblioteca
import pandas as pd

# Definindo a Função para Formatar
def formatar(valor):
    return "{:.2f}%".format(valor)
def visual(v):
    return "{:,.0f}".format(v)

# Criando as Séries
vacinacao = pd.Series([30000000, 25000000, 10000000, 5000000],index = ['2021','2022','2023','2024'])
populacao = pd.Series([213317639, 214477744, 215574303, 216687971],index = ['2021','2022','2023','2024'])

tax_vac = ((vacinacao / populacao) * 100).apply(formatar)
total_tax_vac = (vacinacao.sum()/populacao.tail(1).iloc[0])*100 

# Criando as Visualizações
print('\n--DADOS DA POPULAÇÃO VACINADA--')
print(vacinacao.apply(visual))
print(f'O Acumulado de pessoas vacinadas foi: {vacinacao.sum()}')
print(f'A Média de Pessoas Vacinadas é: {vacinacao.mean():,.0f}')# .mean é para achar a média 

print('\n--DADOS DA POPULAÇÃO--')
print(populacao.apply(visual))
print(f'O Acumulado de Pessoas é: {populacao.tail(1).iloc[0]}')# .tail(1).iloc[0] é usado para pegar o ultimo elemento de uma lista
print(f'A Média de Pessoas é: {populacao.mean():,.0f}') 

print('\n--PERCENTUAL DE PESSOAS VACINADAS POR ANO--')
print(tax_vac)

print(f'\nO Percentual de Pessoas Vacinadas nos Últimos 4 anos foi: {total_tax_vac:.0f}% ')
