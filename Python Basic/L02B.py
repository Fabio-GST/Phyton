# Efetuar a leitura de um valor inteiro positivo ou negativo e apresentar o número lido como sendo um
# valor positivo, ou seja, o programa deverá apresentar o módulo de um número fornecido. Lembre-se
# de verificar se o número fornecido é menor que zero; sendo, multiplique-o por -1. 

A = int(input("\nA: "))

if(A < 0):
    print("O Modulo de A é: ", A * -1)
else:
    print("O Modulo de A é: ", A)