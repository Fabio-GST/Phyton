# Apresentar o total da soma obtida dos cem primeiros números inteiros (1+2+3+4+...+98+99+100). 

soma =0
for i in range(1,101,1):
    soma  += +i

print("O valor da soma é:",soma)