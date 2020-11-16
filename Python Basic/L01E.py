# Efetuar o cálculo e a apresentação do valor de uma prestação em atraso, utilizando a fórmula
# PRESTACAO ← VALOR + (VALOR * TAXA/100) * TEMPO).

Valor = float(input("\nDigite o valor da prestação: "))
Tempo = float(input("\nDigite o tempo de atraso: ")) 
Taxa = float(input("\nDigite o Valor da taxa de juros: "))
Prestação = Valor + (Valor * Taxa/100 )* Tempo
print("O Valor da Prestação em atraso é: ", Prestação)