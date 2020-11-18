# Apresentar os resultados de uma tabuada de multiplicar (de 1 até 10) de um número qualquer. 


x = float(input("Digite um numero: "))

for i in range(1,11,1):
    print(f"{x} x {i} = ",x*i)
