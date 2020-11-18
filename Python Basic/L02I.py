#  Elaborar um programa que efetue a leitura de um número inteiro e apresentar uma mensagem
# informando se o número é par ou ímpar

x = int(input("Digite um numero inteiro: "))
if (x%2 == 0):
    print(f"O numero {x} é par") 
else:
    print(f"O numero {x} é ímpar") 
