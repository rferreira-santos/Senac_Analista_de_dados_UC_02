#2 - O Gerente de uma loja pediu o seu auxílio para que a cada 7 dias, calculasse a média do valor vendido, o maior valor vendido e o menor valor vendido de seus 3 vendedores/as. Pediu para que fosse algo automatizado, pois como ele está em fase de expansão, nos próximos meses mais 4 vendedores serão contratados e sua análise deve estar pronta para isso.
#Ele te passou a venda dos últimos 7 dias, dos/as vendedores/as atuais:
#• Maria: 800,700,1000,900,1200,600,600
#• João: 900,500,1100,1000,900,500,700
#• Manuel: 700,600,900,1200,900,700,400
#Como resultado, ele gostaria de visualizar o Nome do/a vendedor/a e a média de venda, o maior valor vendido e o menor valor vendido, dos últimos 7 dias.

#Importando a Biblioteca
import pandas as pd

# Criando a Tabela Vendedor 
vendedores = [
    ['maria',800,700,1000,900,1200,600,600],
    ['João',900,500,1100,1000,900,500,700],
    ['Manuel',700,600,900,1200,900,700,400]
]

# Criando as Colunas da Tabela Vendedor 
colunas = ['Nome','Segunda','Terça','Quarta','Quinta','Sexta','Sábado','Domingo']

# Criando o DataFrame Vendedor
df_vendedores = pd.DataFrame(vendedores,columns=colunas)

# Exibindo o DataFrame
print(df_vendedores)

# Criando as Métricas
soma_seg = df_vendedores['Segunda'].sum()
media_seg = df_vendedores['Segunda'].mean() 
menor_seg = df_vendedores['Segunda'].min()
maior_seg = df_vendedores['Segunda'].max()
nome_vendedor_seg = df_vendedores[df_vendedores['Segunda']==maior_seg]['Nome'] #Essa metrica busca o melhor vendedor na segunda feira