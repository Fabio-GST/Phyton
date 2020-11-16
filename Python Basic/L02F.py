# Efetuar a leitura de três valores (variáveis A, B e C) e apresentá-los dispostos em ordem crescente. 

A = float(input("A: "))
B = float(input("B: "))
C = float(input("C: "))

if(A <= B and B <= C):
    print(A, B, C)
elif(A < B and C < B):
    print(A, C, B)
elif(B <= A and A <= C):
    print(B, A, C)
elif(A < B and C < A):
    print(B, C, A)
elif(C <= A and A <= B):
    print(C, A, B)
elif(C < A and B < A):
    print(C, B, A)