#script utilizando listas, e separando as notas 
notas = [85,90,65,45,71,28,39,94,48,50]
acima = []
abaixo = []
for i in range(len(notas)):# o comando Len é utilizado para o Range rodar a quantidade de valores que possui a lista
    if notas[i] >= 70:
        acima.append(notas[i])
    else:
        abaixo.append(notas[i])
print('\n--Médias Maiores ou iguais a 70--')
print(acima)
print('\n--Médias menores que a 70--')
print(abaixo)