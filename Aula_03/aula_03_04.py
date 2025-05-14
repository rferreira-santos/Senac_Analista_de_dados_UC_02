#Importando a Biblioteca
import pandas as pd
def formatar(valor):
    return "{:.2f}%".format(valor)

# Criando a Tabela Ocorrências
ocorrencias = [ 
['Rio de Janeiro',6775561,35000], 
['Niteroi',515317,2500], 
['São Gonçalo',1091737,15000], 
['Duque de Caxias',924624,12000], 
['Nova Iguaçu',821128,10000], 
['Belford Roxo',513118,9000], 
['São João de Meriti',471906,8500], 
['Petrópolis',306678,1000], 
['Volta Redonda',273988,2000], 
['Campos dos Goytacazes',507548,4000], 
]

# Criando as Colunas da Tabela Ocorrências 
colunas =['Cidade','Total_Pop','Total_Roubos']

#Criando o DataFrame Vendedor
df_ocorrencias = pd.DataFrame(ocorrencias,columns=colunas)

# Exibindo o DataFrame
print(df_ocorrencias)

# Criando as Métricas

total_roubos = df_ocorrencias['Total_Roubos'].sum()
media_roubos = df_ocorrencias['Total_Roubos'].mean()
total_populacao = df_ocorrencias['Total_Pop'].sum()
media_populacao = df_ocorrencias['Total_Pop'].mean()
maior_roubo = df_ocorrencias['Total_Roubos'].max()
menor_roubo = df_ocorrencias['Total_Roubos'].min()
maior_populacao = df_ocorrencias['Total_Pop'].max()
menor_populacao = df_ocorrencias['Total_Pop'].min()
municipio_maior_roubo = df_ocorrencias[df_ocorrencias['Total_Roubos'] == maior_roubo]['Cidade']
municipio_menor_roubo = df_ocorrencias[df_ocorrencias['Total_Roubos'] == menor_roubo]['Cidade']
municipior_maior_pop = df_ocorrencias[df_ocorrencias['Total_Pop'] == maior_populacao]['Cidade']
municipio_menor_pop = df_ocorrencias[df_ocorrencias['Total_Pop'] == menor_populacao]['Cidade']
total_tx_roubo= ((df_ocorrencias['Total_Roubos']/df_ocorrencias["Total_Pop"])*100).apply(formatar)

# Criando as Visualizações

print('\n------DADOS DA SEGURANÇA PÚBLICA DO RIO DE JANEIRO-------')

print('\n------DADOS DE ROUBO A PEDESTRE-------')
print(f'O Total de roubos a pedestre no último semestre foi de: {total_roubos}')
print(f'A média Total de roubos a pedestre no último semestre foi de: {media_roubos:.0f}')
print(f'O municipio {municipio_maior_roubo.values[0]} teve o maior índice de roubos a pedestres, totalizando {maior_roubo} roubos.')
print(f'O municipio {municipio_menor_roubo.values[0]} teve o maior índice de roubos a pedestres, totalizando {menor_roubo} roubos.')

print('\n------DADOS DA POPULAÇÃO-------')
print(f'A população no estado do Rio de Janeiro no último semestre foi: {total_populacao}')
print(f'A média Total da população no estado do Rio de Janeiro no último semestre foi: {media_populacao:.0f}')
print(f'O municipio {municipior_maior_pop.values[0]} teve o maior índice de Habitantes, totalizando {maior_populacao} Habitantes.')
print(f'O municipio {municipio_menor_pop.values[0]} teve o maior índice de Habitantes, totalizando {menor_populacao} Habitantes.')

print('\n------TAXA DE ROUBO-------')
print(df_ocorrencias['Cidade']+" "+total_tx_roubo)


