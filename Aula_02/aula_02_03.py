#Faça um programa que leia duas séries com 10 números inteiros cada e ao final mostre a soma, a subtração, a multiplicação e a divisão entre elas.
import pandas as pd 
n1 = pd.Series([8,10,25,20,35,4,9,14,80,50])
n2 = pd.Series([4,8,20,31,28,2,6,28,68,70])
soma = [n1 +n2]
subtracao = [n1 -n2]
divisao = [n1 /n2]
multiplicacao = [n1 *n2]
print('\n--A soma dos números é--')
print(soma)
print('\n--A Subtração dos números é--')
print(subtracao)
print('\n--A divisão dos números é--')
print(divisao)
print('\n--A Multiplicação dos números é--')
print(multiplicacao)