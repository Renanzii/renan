numeros = []


while True:
    try:
        numero = float(input("Insira um número (ou qualquer letra para parar): "))
        numeros.append(numero)
    except ValueError:
        break

# Verifica o menor valor na lista
menor_valor = None
for num in numeros:
    if menor_valor is None or num < menor_valor:
        menor_valor = num

# Exibe o menor valor encontrado
if menor_valor is not None:
    print(f"O menor valor na lista é: {menor_valor}")
else:
    print("Nenhum número foi inserido.")