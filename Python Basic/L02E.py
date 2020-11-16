# Efetuar a leitura de três valores (variáveis A, B e C) e efetuar o cálculo da equação completa de
# segundo grau, apresentando as duas raízes, se para os valores informados for possível efetuar o
# referido cálculo. Lembre-se de que a variável A deve ser diferente de zero. 

A = float(input("Digite o valor de A: "))
B = float(input("Digite o valor de B: "))
C = float(input("Digite o valor de C: "))

if(A == 0):
    print("Não é uma equação de 2 grau")

Delta = B**2 - (4*A*C)

print("\n---------------------------------------------------")
if(Delta < 0):
    print("Não existem raizes reais")
elif(Delta == 0):
    print("A raiz da equação é: ",(-B/2*A))
else:
    X1 = (-B + Delta**(1/2))/2*A
    X2 = (-B - Delta**(1/2))/2*A
    print("As raizes reais da equação são:\nX1: ",X1,"\nX2: ",X2)
print("\n---------------------------------------------------")