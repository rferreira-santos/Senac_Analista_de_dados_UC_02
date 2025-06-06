
# Importando a Biblioteca
import pandas as pd
import numpy as np

# Importando a Base de Dados
endereco_dados = 'BASES\Funcionarios.csv'

# Criando o DataFrame Funcionários
df_funcionarios = pd.read_csv(endereco_dados,sep=',',encoding='iso-8859-1')

# Criando um array para o salário
array_salario = np.array(df_funcionarios['Salário'])

# Criando um array para a idade
array_idade = np.array(df_funcionarios['Idade'])

# Criando um array para o tempo de empresa
array_tempo = np.array(df_funcionarios['Tempo'])

# Obtendo as métricas solicitadas
media_salario = np.mean(array_salario)
maior_salario = np.max(array_salario)
menor_salario = np.min(array_salario)
nome_salario = df_funcionarios[df_funcionarios['Salário'] == maior_salario]['Nome']
amplitude_salario = maior_salario - menor_salario
mediana_salario = np.median(array_salario)
distancia_salario = abs((media_salario - mediana_salario)/mediana_salario)

media_idade = np.mean(array_idade)
maior_idade = np.max(array_idade)
menor_idade = np.min(array_idade)
amplitude_idade = maior_idade - menor_idade
nome_velho = df_funcionarios[df_funcionarios['Idade'] == maior_idade]['Nome']
nome_novo = df_funcionarios[df_funcionarios['Idade'] == menor_idade]['Nome']
mediana_idade = np.median(array_idade)
distancia_idade = abs((media_idade - mediana_idade)/mediana_idade)

media_tempo = np.mean(array_tempo)
maior_tempo = np.max(array_tempo)
menor_tempo = np.min(array_tempo)
amplitude_tempo = maior_tempo - menor_tempo
nome_tempo = df_funcionarios[df_funcionarios['Tempo'] == maior_tempo]['Nome']
mediana_tempo = np.median(array_tempo)
distancia_tempo = abs((media_tempo - mediana_tempo)/ mediana_tempo)
qtd_func = np.count_nonzero(array_idade)

# Exibindo as Métricas
print('\n----------- Tabela de Funcionários -------------')
print(df_funcionarios)
print('\n-------- Exibindo os Resultados Solicitados --------')

print(f'A média salarial dos funcionários é R${media_salario:.2f} Reais')
print(f'{nome_salario.values[0]} é o funcionário com maior salário.')
print(f'A Amplitude relativa aos sálarios dos funcionários da empresa é {amplitude_salario} anos')
print(f'A mdiana dos valores salarias é R${mediana_salario:.0f} Reais')
print(f'A distância entre a média e a mediana dos salários dos funcionários é {distancia_salario}')


print(f'\n{nome_velho.values[0]} é o funcionário com mais idade da empresa, com {maior_idade} anos')
print(f'{nome_novo.values[0]} é o funcionário com menos idade da empresa, com {menor_idade} anos')
print(f'A Amplitude relativa a idade dos funcionários da empresa é {amplitude_idade} anos')
print(f'A média das idades dos funcionários é {media_idade:.0f} anos')
print(f'A mdiana das idades dos funcionários é {mediana_idade:.0f} anos')
print(f'A distância entre a média e a mediana das idades dos funcionários é {distancia_idade}')

print(f'\n{nome_tempo.values[0]} é o funcionário com mais tempo de empresa')
print(f'O Funcionário com maior tempo de empresa possui {maior_tempo} anos')
print(f'O Funcionário com menor tempo de empresa possui {menor_tempo} anos')
print(f'A Amplitude relativa ao tempo de empresa é {amplitude_tempo} anos')
print(f'O tempo médio dos funcionários na empresa é {media_tempo:.0f} anos')
print(f'A mdiana do tempo de empresa dos funcionários é {mediana_tempo:.0f} anos')
print(f'A distância entre a média e a mediana do tempo de empresa dos funcionários é {distancia_tempo}')

print(f'\nA quantidade de funcionários na empresa são {qtd_func}')