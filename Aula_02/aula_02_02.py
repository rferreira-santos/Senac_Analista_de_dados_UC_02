#script utilizando Séries.
import pandas as pd 
notas = pd.Series([85,90,65,45,71,28,39,94,48,50])
acima = notas[notas >=70]
abaixo = notas[notas < 70]
print('\n--Médias Maiores ou iguais a 70--')
print(acima)
print('\n--Médias menores que a 70--')
print(abaixo)