# Calcular e apresentar o valor do volume de uma lata de óleo, utilizando a fórmula:
# Volume = PI* Raio 2* Altura 

Raio = float(input("\nDigite o raio: "))
Altura = float(input("\nDigite a altura: "))
PI = 3.14
Volume = PI * Raio**2 * Altura
print("O volume é: ",Volume)
