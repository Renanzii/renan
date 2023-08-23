num_list =int(input("Digite os numeros da lista separados: "))

num_pares = 0
num_impares = 0

for num in range(1,num_list):
    if num % 2 == 0:
        num_pares = num_pares + 1
    else:
        num_impares = num_impares + 1

print(f"quantidade de numeros pares {num_pares}")  
print(f"quantidade de numeros impares {num_impares}")     
