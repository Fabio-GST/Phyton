# Ler quatro valores referentes a quatro notas escolares de um aluno e imprimir uma mensagem
# dizendo que o aluno foi aprovado, se o valor da média escolar for maior ou igual a 5. Se o aluno não
# foi aprovado, indicar uma mensagem informando esta condição. Apresentar junto das mensagens o
# valor da média do aluno para qualquer condição

Nota1 = float(input("Nota 1: "))
Nota2 = float(input("Nota 2: "))
Nota3 = float(input("Nota 3: "))
Nota4 = float(input("Nota 4: "))

Media = (Nota1+Nota2+Nota3+Nota4)/4
print("\n---------------------------------------------------")
if(Media >= 5):
    print("\tO aluno foi aprovado\n\tMédia Final: ", Media)
else:
    print("\tO aluno foi reprovado\n\tMédia Final: ", Media)
print("\n---------------------------------------------------")