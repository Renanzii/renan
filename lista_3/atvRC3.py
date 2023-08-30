import random


numero_secreto = random.randint(1, 100)


while True:
    
    tentativa = int(input("Digite um número: "))
    
    
    if tentativa == numero_secreto:
        print("Parabéns, você acertou!")
        break
    elif tentativa < numero_secreto:
        print("Tente um número maior.")
    else:
        print("Tente um número menor.")