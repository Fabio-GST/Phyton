# Efetuar a leitura de cinco números inteiros e identificar o maior e o menor valores. 

Num = []
for i in range (5):
    Num.append(int(input("Digite o  Numero: ")))

print("O menor numero é: ",min(Num))
print("O maior Numero é: ",max(Num))

