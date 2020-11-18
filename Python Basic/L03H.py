# Elaborar um programa que apresente os valores de conversão de graus Celsius em Fahrenheit, de
# 10 em 10 graus, iniciando a contagem em 10 graus Celsius e finalizando em 100 graus Celsius. O
# programa deve apresentar os valores das duas temperaturas. A fórmula de conversão
# é f = (9C+160)/5 sendo F a temperatura em Fahrenheit e C a temperatura em Celsius. 

print("| ºC | ºF   |")
for C in range (10,101,10):
    F = (9*C+160)/5
    print(f"| {C} | {F} |")