# Efetuar o cálculo da quantidade de litros de combustível gasta em uma viagem, utilizando um
# automóvel que faz 12 Km por litro. Para obter o cálculo, o usuário deve fornecer o tempo gasto
# (TEMPO) e a velocidade média (VELOCIDADE) durante a viagem. Desta forma, será possível obter a
# distância percorrida com a fórmula DISTANCIA ← TEMPO * VELOCIDADE. Possuindo o valor da
# distância, basta calcular a quantidade de litros de combustível utilizada na viagem com a fórmula
# LITROS_USADOS ← DISTANCIA / 12. Ao final, o programa deve apresentar os valores da velocidade
# média (VELOCIDADE), tempo gasto na viagem (TEMPO), a distancia percorrida (DISTANCIA) e a
# quantidade de litros (LITROS_USADOS) utilizada na viagem.

Tempo = float(input("\nDigite o tempo gasto na viagem: "))
Velocidade = float(input("\nDigite a velocidade média durante a viagem: "))
Distancia = Velocidade * Tempo
Litros_Usados = Distancia / 12
print("--------------------------------------------------------")
print("\nA Velocidade média foi: ", Velocidade)
print("\nO tempo gasto na viagem foi: ", Tempo)
print("\nA distancia percorrida foi: ",Distancia)
print("\nA quantidade de Litros usados foi: ",Litros_Usados)
print("--------------------------------------------------------")