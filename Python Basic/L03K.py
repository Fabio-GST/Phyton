# Elaborar um programa que possibilite calcular a área total de uma residência (sala, cozinha,
# banheiro, quartos, área de serviço, quintal, garagem, etc.). O programa deve solicitar a entrada do
# nome, a largura e o comprimento de um determinado cômodo. Em seguida, deve apresentar a área 
# do cômodo lido e também uma mensagem solicitando do usuário a confirmação de continuar
# calculando novos cômodos. Caso o usuário responda “NAO”, o programa deve apresentar o valor
# total acumulado da área residencial. 


Nome = []
area = []

while(True):
    Nome.append(input(print("Digite o nome do cômodo: ")))
    larg = float(input("Digite a largura: "))
    comp = float(input("Digite o comprimento: "))
    area.append(larg*comp) 
    resp = input(print("Deseja Adicionar um Novo cômodo?"))
    if (resp=="NAO"):
        break
for i in range (len(Nome)):
    print("\n---------------------------------------------------")
    print("Nome: ",Nome[i])
    print("Area: ",area[i])
    print("\n---------------------------------------------------")
print("Area total:",sum(area))