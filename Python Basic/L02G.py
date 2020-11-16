# Efetuar a leitura de quatro números inteiros e apresentar os números que são divisíveis por 2 e 3

A = int(input("A: "))
B = int(input("B: "))
C = int(input("C: "))
D = int(input("D: "))
print("--------------------------------------------------------")
if(A%2 == 0 or A%3 == 0 and A != 0):
    print(A)
if(B%2 == 0 or B%3 == 0 and B != 0):
    print(B)
if(C%2 == 0 or C%3 == 0 and C != 0):
    print(C)
if(D%2 == 0 or D%3 == 0 and D != 0):
    print(D)
print("--------------------------------------------------------")