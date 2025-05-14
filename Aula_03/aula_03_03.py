#Importando a Biblioteca
import pandas as pd

# Criando a Tabela Vendedor 
vendedores = [
['Ana','F',28,120], 
['Bruno','M',34,150],
['Carlos','M',45,110], 
['Diana','F',30,95], 
['Eduardo','M',40,130], 
['Fernanda','F',29,140], 
['Gustavo','M',38,105], 
['Helena','F',31,125], 
['Igor','M',27,100], 
['Juliana','F',33,135], 
]
# Criando as Colunas da Tabela Vendedor 
colunas =['Nome','Sexo','Idade','Vendas']

#Criando o DataFrame Vendedor
df_vendedores = pd.DataFrame(vendedores,columns=colunas)

# Exibindo o DataFrame
print(df_vendedores)

# Criando as Métricas
soma_vendas = df_vendedores['Vendas'].sum()
media_vendas = df_vendedores['Vendas'].mean()
media_idade = df_vendedores['Idade'].mean()
maior_idade = df_vendedores['Idade'].max()
menor_idade = df_vendedores['Idade'].min()
maior_vendas = df_vendedores['Vendas'].max()
menor_vendas = df_vendedores['Vendas'].min()
melhor_vendedor = df_vendedores[df_vendedores['Vendas'] == maior_vendas]['Nome']
pior_vendedor = df_vendedores[df_vendedores['Vendas'] == menor_vendas]['Nome']
vendas_fem = df_vendedores[df_vendedores['Sexo'] == 'F']['Vendas'].sum
vendas_mas = df_vendedores[df_vendedores['Sexo'] == 'M']['Vendas'].sum

# Criando as Visualizações

print('\n------DADOS DOS VENDEDORES-------')
print(f'A quantidade total de vendas foi {soma_vendas}')
print(f'A quantidade média de vendas foi {media_vendas:.0f}')
print(f'A média de idade dos vendedores é {media_idade:.0f}')
print(f'A maior idade encontrada foi {maior_idade}')
print(f'A menor idade encontrada foi {menor_idade}')
print(f'A quantidade total de vendas realizada pelas vendedoras foi {vendas_fem}')
print(f'A quantidade total de vendas realizada pelos vendedores foi {vendas_mas}')
print(f'Sr(a) {melhor_vendedor.values[0]} vendeu {maior_vendas} produtos, tendo o melhor desempenho') # .values[0] posto depois da variável significa uma mascara para exibir apenas o nome sem a idexação do dataframe 
print(f'Sr(a) {pior_vendedor.values[0]} vendeu {menor_vendas} produtos, tendo o pior desempenho')

