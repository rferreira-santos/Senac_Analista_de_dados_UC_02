#2 - O Gerente de uma loja pediu o seu auxílio para que a cada 7 dias, calculasse a média do valor vendido, o maior valor vendido e o menor valor vendido de seus 3 vendedores/as. Pediu para que fosse algo automatizado, pois como ele está em fase de expansão, nos próximos meses mais 4 vendedores serão contratados e sua análise deve estar pronta para isso.
#Ele te passou a venda dos últimos 7 dias, dos/as vendedores/as atuais:
#• Maria: 800,700,1000,900,1200,600,600
#• João: 900,500,1100,1000,900,500,700
#• Manuel: 700,600,900,1200,900,700,400
#Como resultado, ele gostaria de visualizar o Nome do/a vendedor/a e a média de venda, o maior valor vendido e o menor valor vendido, dos últimos 7 dias.

#Importando a Biblioteca
import pandas as pd

# Definindo a Função para Formatar
def formatar(valor):
    return "{:.2f}%".format(valor)
def visual(v):
    return "{:,.0f}".format(v)

# Criando as Séries
maria = pd.Series([800,700,1000,900,1200,600,600],index = ['Segunda','Terça','Quarta','Quinta','Sexta','Sábado','Domingo']) 
joao = pd.Series([900,500,1100,1000,900,500,700],index = ['Segunda','Terça','Quarta','Quinta','Sexta','Sábado','Domingo'])
manuel = pd.Series([700,600,900,1200,900,700,400],index = ['Segunda','Terça','Quarta','Quinta','Sexta','Sábado','Domingo'])

# Criando as Visualizações
print('\n------DADOS DA VENDEDORA MARIA-------')
print(maria)
print(f'\nO Total vendido foi:{maria.sum()}')
print(f'A Média vendida foi:{maria.mean():.0f}')
print(f'O Menor Valor vendido foi:{maria.min()}')
print(f'O Maior Valor vendido foi:{maria.max()}')

print('\n------DADOS DA VENDEDOR JOÃO-------')
print(joao)
print(f'\nO Total vendido foi:{joao.sum()}')
print(f'A Média vendida foi:{joao.mean():.0f}')
print(f'O Menor Valor vendido foi:{joao.min()}')
print(f'O Maior Valor vendido foi:{joao.max()}')

print('\n------DADOS DA VENDEDOR MANUEL-------')
print(manuel)
print(f'\nO Total vendido foi:{manuel.sum()}')
print(f'A Média vendida foi:{manuel.mean():.0f}')
print(f'O Menor Valor vendido foi:{manuel.min()}')
print(f'O Maior Valor vendido foi:{manuel.max()}')