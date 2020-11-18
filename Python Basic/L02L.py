# Elaborar um programa que efetue a leitura do nome e do sexo de uma pessoa, apresentando com
# saída uma das seguintes mensagens: "Ilmo Sr.", se o sexo informado como masculino, ou a
# mensagem "Ilma Sra.", para o sexo informado como feminino. Apresente também junto da
# mensagem de saudação o nome previamente informado. 

Nome = input("Digite seu Nome: ")
sexo = input("Digite o seu sexo (masculino ou feminino): ")

if(sexo == 'masculino'):
    print(f"Ilmo Sr. {Nome}")
elif(sexo == 'feminino'):
    print(f"Ilma Sra. {Nome}")
else:
    print("Sexo invalido")