def divis(v1, v2):
 if v2 == 0:
  print("nao existe") 
  return
 return v1/v2


def ler():
 a= int(input("digite o valor:"))
 return a

v1 = ler()
v2 = ler()

x = v1/v2
print(f"seu valor e{x}")