# Elaborar um programa que efetue a leitura de 10 valores numéricos e apresente no final o total do
# somatório e a média aritmética dos valores lidos. 
soma = 0
media = 0
for i in range (10):
    x = float (input("Digite Um numero: "))
    soma += x
    media += x / 10
print("A soma dos valores é : ",soma)
print("A Media dos valores é : ",media)