#Escreva um programa que leia uma série com 10 idades e ao final separe as que estão iguais e acima de 18 anos das que estão abaixo de 18 anos.
import pandas as pd 
idade = pd.Series([10,18,26,8,35,34,16,17,64,70])
acima = idade[idade >=18]
abaixo = idade[idade < 18]



print('\n--Idade Maiores ou iguais a 18 anos--')
print(acima.to_string(index=False))#.to_string(index=false) serve para remover a coluna indice da lista 
print('\n--Idade Menores que a 18 anos--')
print(abaixo.to_string(index=False))