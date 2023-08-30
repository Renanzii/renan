notas = []
continuar = True

while continuar:
    nota = float(input("Digite a nota do aluno (ou digite -1 para parar): "))
    
    if nota == -1:
        continuar = False
    else:
        notas.append(nota)

if len(notas) > 0:
    media = sum(notas) / len(notas)
    print("A média das notas é:", media)
else:
    print("Nenhuma nota foi inserida.")