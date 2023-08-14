a = 2
b = "vai meu filho"
print(a)
print(type(a))

print(b)
print(type(b))
b = a
print(b)
print(type (b))
if a > 2:
    print("a é maior que 2")
elif a==2:
    print(" a é igual a 2")
else:
    print("a não é menor que 2")


palavra = " vai "
palavra2 = " funcionar "
palavra3 = " pr favor "
print(palavra + palavra2 + palavra3)
print(palavra + palavra2 + palavra3 + str(a))
c = "3"
print(type(c))
c = int(c)
print(type(c))

idade = int (input("Digite sua idade: "))
print(idade)
if idade >= 18:
    print(" e maior de idade")
else:
    print("e menor de idade ")