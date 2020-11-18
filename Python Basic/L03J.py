# Elaborar um programa que apresente os resultados da soma e da média aritmética dos valores
# pares situados na faixa numérica de 50 a 70. 

soma = 0
j = 0
for i in range (50,71,2):
    soma += i
    j +=1
media = soma / j
print("A soma dos valores é : ",soma)
print("A Media dos valores é : ",media)
