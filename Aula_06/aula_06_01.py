import pandas as pd
import numpy as np

print('---- OBTENDO DADOS ----')

# Importando a base de dados Enem.csv    
endereco_dados = 'BASES\ENEM_2014_2023.csv'

# Criando o DataFrame Enem
df_enem_geral = pd.read_csv(endereco_dados,sep=';',encoding='utf-8')
df_enem = df_enem_geral[['Estado','Total']]
df_enem_top_10 = df_enem_geral.sort_values(by='Total',ascending=False)[['Estado','Total']]

# Exibindo a base de dados Enem
print('\n---- EXIBINDO A BASE DE DADOS -----')
print(df_enem.to_string(index=False))

# Criando o array do valor total
array_enem_total = np.array(df_enem["Total"])

# Obtendo a média do valor total
media_total = np.mean(array_enem_total)

# Obtendo a mediana do valor total
mediana_total = np.median(array_enem_total)

# Obtendo a distância entre a média e a mediana do valor total
distancia_total = abs((media_total - mediana_total) / mediana_total)

# Obtendo o menor valor total
minimo_total = np.min(array_enem_total)

# Obtendo o maior valor total
maximo_total = np.max(array_enem_total)

# Obtendo a amplitude dos valores total
amplitude_total = maximo_total - minimo_total

# Obtendo o valor do 1º quartil(25%) do valor total
q1_total = np.quantile(array_enem_total,0.25,method='weibull')

# Obtendo o valor do 2º quartil(50%) do valor total
q2_total = np.quantile(array_enem_total,0.50,method='weibull')

# Obtendo o valor do 3º quartil(75%) do valor total
q3_total = np.quantile(array_enem_total,0.75,method='weibull')

# Obtendo o valor do iqr do valor total
iqr_total = q3_total - q1_total

# Obtendo o limite inferior do valor total
limite_inferior_total = q1_total - (1.5 * iqr_total)

# Obtendo o limite superior do valor total
limite_superior_total = q3_total + (1.5 * iqr_total)    

# Obtendo os outliers inferiores do valor total
df_total_outliers_inferiores = df_enem[df_enem['Total'] < limite_inferior_total]

# Obtendo os outliers superiores do valor total
df_total_outliers_superiores = df_enem[df_enem['Total'] > limite_superior_total]  

# Obtendo os dados sobre os estados com maiores e menores inscritos
estado_maior = df_enem[df_enem['Total'] == maximo_total]['Estado'].values[0]
estado_menor = df_enem[df_enem['Total'] == minimo_total]['Estado'].values[0]
percentual_total = ((maximo_total - minimo_total) / minimo_total) * 100

# Exibindo os dados sobre o valor total
print("\n-- OBTENDO AS MEDIDAS DESCRITIVAS --")
print('Medidas de Tendência Central')
print(f"A média do valor total é {media_total:.0f}")
print(f"A mediana do valor total é {mediana_total:.0f}")
print(f"A distância entre a média e a mediana do valor total é {distancia_total}")
print(f"O menor valor do valor total é {minimo_total:.0f}")
print(f"O maior valor do valor total é {maximo_total:.0f}")
print(f"A amplitude dos valores do valor total é {amplitude_total:.0f}")
print(f'O valor do 1º quartil(25%) do valor total é {q1_total:.0f}')
print(f'O valor do 2º quartil(50%) do valor total é {q2_total:.0f}')
print(f'O valor do 3º quartil(75%) do valor total é {q3_total:.0f}')
print(f'O valor do iqr do valor total é {iqr_total:.0f}')
print(f'O limite inferior do valor total é {limite_inferior_total:.0f}')
print(f'O limite superior do valor total é {limite_superior_total:.0f}')
if len(df_total_outliers_inferiores) == 0:
    print('\nNão existem outliers inferiores')
else:
    print('\n------------ Outliers Inferiores ---------------')
    print(df_total_outliers_inferiores)
if len(df_total_outliers_superiores) == 0:
    print('\nNão existem outliers superiores')
else:
    print('\n------------ Outliers Superiores ---------------')
    print(df_total_outliers_superiores)

print(f'\nO estado com a maior quantidade de inscritos na série histórica é {estado_maior}')
print(f'O estado com a menor quantidade de inscritos na série histórica é {estado_menor}')
print(f'O percentual de inscritos no estado de {estado_maior} em relação ao estado de {estado_menor} é {percentual_total:.0f}%')

# Exibindo um rankig com os estados com maior quantidade de inscritos
print('\n---- EXIBINDO UM RANKING COM OS ESTADOS COM MAIOR QUANTIDADE DE INSCRITOS -----')
print(df_enem_top_10.head(10).to_string(index=False))

print('\n---- FIM DO PROGRAMA ----')