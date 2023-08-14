massa_da_pessoa = int(input("quantos kg você tem: "))
altura_da_pessoa = float(input("qual e a sua altura: "))


IMC = massa_da_pessoa / altura_da_pessoa ** 2

print(f"o seu IMC vai ser {IMC}")