# Ler dois valores (inteiros, reais ou caracteres) para as variáveis A e B, e efetuar a troca dos valores de
# forma que a variável A passe a possuir o valor da variável B e a variável B passe a possuir o valor da
# variável A. Apresentar os valores trocados


A = input("\nDigite o valor de A: ")
B = input("\nDigite o valor de B: ")
C = B 
B = A
A = C
print("---------------------------------------------------")
print("\nO valor de A é: ", A)
print("\nO valor de B é: ", B)
print("---------------------------------------------------")
