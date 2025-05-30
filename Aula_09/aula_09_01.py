import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print('\n---- OBTENDO DADOS ----')

endereco_dados = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'

# Criando o DataFrame Ocorrencias
df_ocorrencias = pd.read_csv(endereco_dados,sep=';',encoding='iso-8859-1')

# Criando o DataFrame Roubo de Veiculo
df_roubo_veiculo = df_ocorrencias[['cisp','roubo_veiculo']]
df_roubo_veiculo = df_roubo_veiculo.groupby(['cisp']).sum(['roubo_veiculo']).reset_index()

# Criando o DataFrame Furto de Veiculo
df_furto_veiculo = df_ocorrencias[['cisp','furto_veiculos']]
df_furto_veiculo = df_furto_veiculo.groupby(['cisp']).sum(['furto_veiculos']).reset_index()

# Criando o DataFrame Recuperação de Veiculo
df_recuperacao_veiculo = df_ocorrencias[['cisp','recuperacao_veiculos']]
df_recuperacao_veiculo = df_recuperacao_veiculo.groupby(['cisp']).sum(['recuperacao_veiculos']).reset_index()

# Criando o DataFrame Roubo e Furto de Veiculo
df_roubo_furto_veiculo = df_ocorrencias[['cisp','roubo_veiculo','furto_veiculos']]
df_roubo_furto_veiculo = df_roubo_furto_veiculo.groupby(['cisp']).sum(['roubo_veiculo','furto_veiculos']).reset_index()

# Criando Array Roubo de Veiculo
array_roubo_veiculo = np.array(df_roubo_veiculo["roubo_veiculo"])

# Criando Array Furto de Veiculo
array_furto_veiculo = np.array(df_furto_veiculo["furto_veiculos"])

# Criando Array Recuperação de Veiculo
array_recuperacao_veiculo = np.array(df_recuperacao_veiculo["recuperacao_veiculos"])   

# Obtendo os quartis das recuperações de veiculo
quartil_1_recuperacao_veiculo = np.percentile(array_recuperacao_veiculo,25)
quartil_2_recuperacao_veiculo = np.percentile(array_recuperacao_veiculo,50)
quartil_3_recuperacao_veiculo = np.percentile(array_recuperacao_veiculo,75)
iqr_recuperacao_veiculo = quartil_3_recuperacao_veiculo - quartil_1_recuperacao_veiculo

# Obtendo os quartis dos Roubo de Veiculo
quartil_1_roubo_veiculo = np.percentile(array_roubo_veiculo,25) 
quartil_2_roubo_veiculo = np.percentile(array_roubo_veiculo,50)
quartil_3_roubo_veiculo = np.percentile(array_roubo_veiculo,75)
iqr_roubo_veiculo = quartil_3_roubo_veiculo - quartil_1_roubo_veiculo

#Obtendo os quartis dos Furto de Veiculo
quartil_1_furto_veiculo = np.percentile(array_furto_veiculo,25)
quartil_2_furto_veiculo = np.percentile(array_furto_veiculo,50)
quartil_3_furto_veiculo = np.percentile(array_furto_veiculo,75)
iqr_furto_veiculo = quartil_3_furto_veiculo - quartil_1_furto_veiculo


# Correlação entre Roubo de Veiculo e Furto de Veiculo
# 0.9 a 1.0 (positiva ou negativa) = Muito forte correlação
# 0.7 a 0.9 (positiva ou negativa) = Forte correlação
# 0.5 a 0.7 (positiva ou negativa) = Moderada correlação
# 0.3 a 0.5 (positiva ou negativa) = Fraca correlação
# 0.0 a 0.3 (positiva ou negativa) = Sem correlação

corr_roubo_furto_veiculo = np.corrcoef(df_roubo_furto_veiculo['roubo_veiculo'], df_roubo_furto_veiculo['furto_veiculos'])[0,1]
corr_roubo_recuperacao_veiculo = np.corrcoef(df_roubo_veiculo['roubo_veiculo'], df_recuperacao_veiculo['recuperacao_veiculos'])[0,1]
corr_furto_recuperacao_veiculo = np.corrcoef(df_furto_veiculo['furto_veiculos'], df_recuperacao_veiculo['recuperacao_veiculos'])[0,1]

# Indentificando os outliers superiores e inferiores dos Roubo de Veiculo
limite_superior_roubo_veiculo = quartil_3_roubo_veiculo + (1.5 * (quartil_3_roubo_veiculo - quartil_1_roubo_veiculo))
limite_inferior_roubo_veiculo = quartil_1_roubo_veiculo - (1.5 * (quartil_3_roubo_veiculo - quartil_1_roubo_veiculo))

# Identificando os outliers superiores e inferiores dos Furto de Veiculo
limite_superior_furto_veiculo = quartil_3_furto_veiculo + (1.5 * (quartil_3_furto_veiculo - quartil_1_furto_veiculo))
limite_inferior_furto_veiculo = quartil_1_furto_veiculo - (1.5 * (quartil_3_furto_veiculo - quartil_1_furto_veiculo))

# Identificando os outliers superiores e inferiores das Recuperação de Veiculo
limite_superior_recuperacao_veiculo = quartil_3_recuperacao_veiculo + (1.5 * (quartil_3_recuperacao_veiculo - quartil_1_recuperacao_veiculo))
limite_inferior_recuperacao_veiculo = quartil_1_recuperacao_veiculo - (1.5 * (quartil_3_recuperacao_veiculo - quartil_1_recuperacao_veiculo))

# Filtrando o DataFrame roubo de veiculo
df_roubo_veiculo_outliers_superiores = df_roubo_veiculo[df_roubo_veiculo['roubo_veiculo'] > limite_superior_roubo_veiculo]
df_roubo_veiculo_outliers_inferiores = df_roubo_veiculo[df_roubo_veiculo['roubo_veiculo'] < limite_inferior_roubo_veiculo]

# Filtrando o DataFrame furto de veiculo
df_furto_veiculo_outliers_superiores = df_furto_veiculo[df_furto_veiculo['furto_veiculos'] > limite_superior_furto_veiculo]
df_furto_veiculo_outliers_inferiores = df_furto_veiculo[df_furto_veiculo['furto_veiculos'] < limite_inferior_furto_veiculo]

# Filtrando o DataFrame recuperacao de veiculo
df_recuperacao_veiculo_outliers_superiores = df_recuperacao_veiculo[df_recuperacao_veiculo['recuperacao_veiculos'] > limite_superior_recuperacao_veiculo]
df_recuperacao_veiculo_outliers_inferiores = df_recuperacao_veiculo[df_recuperacao_veiculo['recuperacao_veiculos'] < limite_inferior_recuperacao_veiculo]

print('\n- Visualizando os dados sobre os roubos de veiculo -')
plt.subplots(2,3,figsize=(10,7))
plt.suptitle('Análise dos Dados sobre os Roubos de Veículos')

 #Visualizando Gráfico dos Outliers dos Roubos de Veículos
df_roubo_veiculo_outliers_superiores_order = df_roubo_veiculo_outliers_superiores.sort_values(by='roubo_veiculo',ascending=True)
plt.subplot(2,3,1)
plt.title('Gráfico dos Outliers dos Roubos de Veículos')
plt.barh(df_roubo_veiculo_outliers_superiores_order['cisp'].astype(str),df_roubo_veiculo_outliers_superiores_order['roubo_veiculo'])

#Visualizando Gráfico dos Outliers dos Furto de Veículos
df_furto_veiculo_outliers_superiores_order = df_furto_veiculo_outliers_superiores.sort_values(by='furto_veiculos',ascending=True)
plt.subplot(2,3,2)
plt.title('Gráfico dos Outliers dos Furto de Veículos')
plt.barh(df_furto_veiculo_outliers_superiores_order['cisp'].astype(str),df_furto_veiculo_outliers_superiores_order['furto_veiculos'])

# Visualizando Gráfico dos Outliers das Recuperação de Veículos
df_recuperacao_veiculo_outliers_superiores_order = df_recuperacao_veiculo_outliers_superiores.sort_values(by='recuperacao_veiculos',ascending=True)
plt.subplot(2,3,3)
plt.title('Gráfico dos Outliers das Recuperação de Veículos')
plt.barh(df_recuperacao_veiculo_outliers_superiores_order['cisp'].astype(str),df_recuperacao_veiculo_outliers_superiores_order['recuperacao_veiculos'])

# Visualizando Grafico das correlacoes
plt.subplot(2,3,4)
plt.title('Correlação entre os Roubos de Veículos e Furto de Veículos')
plt.scatter(df_furto_veiculo['furto_veiculos'], df_roubo_veiculo['roubo_veiculo'])
plt.xlabel('Furto de Veículos')
plt.ylabel('Roubos de Veículos')

plt.subplot(2,3,5)
plt.title('Correlação entre os Roubos de Veículos e Recuperação de Veículos')
plt.scatter(df_recuperacao_veiculo['recuperacao_veiculos'], df_roubo_veiculo['roubo_veiculo'])
plt.xlabel('Recuperação de Veículos')
plt.ylabel('Roubos de Veículos')

plt.subplot(2,3,6)
plt.title('Correlação entre os Furto de Veículos e Recuperação de Veículos')
plt.scatter(df_recuperacao_veiculo['recuperacao_veiculos'], df_furto_veiculo['furto_veiculos'])
plt.xlabel('Recuperação de Veículos')
plt.ylabel('Furto de Veículos')

plt.show()
