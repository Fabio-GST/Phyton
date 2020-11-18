# Elaborar um programa que apresente no final o somatório dos valores pares existentes na faixa de
# 1 até 500. 

soma = 0
for i in range(2,501,2):
    soma += i
print("O valor da soma é:",soma)
