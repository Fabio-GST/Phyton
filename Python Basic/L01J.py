# Elaborar um programa que efetue a apresentação do valor da conversão em real de um valor lido em
# dólar. O programa deve solicitar o valor da cotação do dólar e também a quantidade de dólares
# disponível com o usuário, para que seja apresentado o valor em moeda brasileira.

Dolar = float(input("\nDigite o valor em Dollar: "))
Taxa =  float(input("\nDigite o valor da cotação do dollar: "))
print("\nO valor em reais é: ", (Dolar * Taxa ))