ang_1 = int(input("Digite o valor do primeiro ângulo: "))
ang_2 = int(input("Digite o valor do segundo ângulo: "))
ang_3 = int(input("Digite o valor do terceiro ângulo: "))

soma_angulos = ang_1 + ang_2 + ang_3

if soma_angulos == 180:
    if ang_1 < 90 and ang_2 < 90 and ang_3 < 90:
        resultado = "Acutângulo"
    elif ang_1 == 90 or ang_2 == 90 or ang_3 == 90:
        resultado = "Retângulo"
    elif ang_1 > 90 or ang_2 > 90 or ang_3 > 90:
        resultado = "Obtusângulo"
else:
    resultado = "Os ângulos informados não formam um triângulo"

print(resultado)