import pandas as pd
import numpy as np

print('---- OBTENDO DADOS ----')

# Importando a base de dados de ocorrências    
endereco_dados = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'

# Criando o DataFrame ocorrências
df_ocorrencias = pd.read_csv(endereco_dados,sep=';',encoding='iso-8859-1')
df_hom_doloso = df_ocorrencias[['ano','hom_doloso']]
df_hom_doloso = df_hom_doloso.groupby(['ano']).sum(['hom_doloso']).reset_index()
df_hom_doloso = df_hom_doloso.drop(df_hom_doloso.index[22])
# Exibindo a base de dados ocorrências
print('\n---- EXIBINDO A BASE DE DADOS -----')
print(df_hom_doloso)

# Criando o array do Homicidio Doloso
array_hom_doloso = np.array(df_hom_doloso["hom_doloso"])

# Obtendo a média do valor total
media_hom_doloso = np.mean(array_hom_doloso) 

# Obtendo a mediana do valor total  
mediana_hom_doloso = np.median(array_hom_doloso)

# Obtendo a distância entre a média e a mediana do valor total
distancia_hom_doloso = abs((media_hom_doloso - mediana_hom_doloso) / mediana_hom_doloso) 

# Obtendo o menor valor total   
minimo_hom_doloso = np.min(array_hom_doloso)

# Obtendo o maior valor total   
maximo_hom_doloso = np.max(array_hom_doloso)    

# Obtendo a amplitude dos valores total
amplitude_hom_doloso = maximo_hom_doloso - minimo_hom_doloso    

# Obtendo o valor do 1º quartil(25%) do valor total
q1_hom_doloso = np.percentile(array_hom_doloso, 25)

# Obtendo o valor do 3º quartil(75%) do valor total
q3_hom_doloso = np.percentile(array_hom_doloso, 75) 

# Obtendo a distância interquartil do valor total
distancia_interquartil_hom_doloso = q3_hom_doloso - q1_hom_doloso        

# Obtendo o valor do iqr do valor total
iqr_hom_doloso = q3_hom_doloso - q1_hom_doloso

# Obtendo o limite inferior do valor total
limite_inferior_hom_doloso = q1_hom_doloso - (1.5 * iqr_hom_doloso)

# Obtendo o limite superior do valor total    
limite_superior_hom_doloso = q3_hom_doloso + (1.5 * iqr_hom_doloso)    

# Obtendo os outliers inferiores do valor total
df_hom_doloso_outliers_inferiores = df_hom_doloso[df_hom_doloso['hom_doloso'] < limite_inferior_hom_doloso]

# Obtendo os outliers superiores do valor total 
df_hom_doloso_outliers_superiores = df_hom_doloso[df_hom_doloso['hom_doloso'] > limite_superior_hom_doloso]

# Exibindo os dados sobre o valor total
print("\n-- OBTENDO AS MEDIDAS DESCRITIVAS --") 
print('Medidas de Tendência Central')
print(f"A média do valor total é {media_hom_doloso:.0f}")
print(f"A mediana do valor total é {mediana_hom_doloso:.0f}")
print(f"A distância entre a média e a mediana do valor total é {distancia_hom_doloso}")
print(f"O menor valor do valor total é {minimo_hom_doloso:.0f}")
print(f"O maior valor do valor total é {maximo_hom_doloso:.0f}")
print(f"A amplitude dos valores do valor total é {amplitude_hom_doloso:.0f}")
print(f'O valor do 1º quartil(25%) do valor total é {q1_hom_doloso:.0f}')
print(f'O valor do 3º quartil(75%) do valor total é {q3_hom_doloso:.0f}')    
print(f"A distância interquartil do valor total é {distancia_interquartil_hom_doloso}")
print(f'O valor do iqr do valor total é {iqr_hom_doloso:.0f}')    
print(f'O limite inferior do valor total é {limite_inferior_hom_doloso:.0f}')
print(f'O limite superior do valor total é {limite_superior_hom_doloso:.0f}')
if len(df_hom_doloso_outliers_inferiores) == 0:
    print('\nNão existem outliers inferiores')
else:
    print('\n------------ Outliers Inferiores ---------------')    
    print(df_hom_doloso_outliers_inferiores)    
if len(df_hom_doloso_outliers_superiores) == 0:                                                                
    print('\nNão existem outliers superiores')
else:
    print('\n------------ Outliers Superiores ---------------')
    print(df_hom_doloso_outliers_superiores)                                                                                                                                                                                                                                      