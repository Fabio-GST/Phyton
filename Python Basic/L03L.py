# Elaborar um programa que efetue a leitura de valores positivos inteiros até que um valor negativo
# seja informado. Ao final devem ser apresentados o maior e o menor valores informados pelo
# usuário.

Num = []
i = 0
while (True):
    Num.append(int(input("Digite o numero: ")))
    if(Num[i] < 0):
        break
    i +=1
print("O menor numero é: ",min(Num))
print("O maior Numero é: ",max(Num))
