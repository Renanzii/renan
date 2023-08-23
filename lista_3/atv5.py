quant_num = int (input("insira uma lista de numeros separados: "))
numeros = []  

for i in range(0, quant_num):
    numeros.append(int(input('digite um numero:')))


maior = 0

for c in numeros:
    if c > maior:
        maior = c

print(f" o maior valor na lista é {maior}")
