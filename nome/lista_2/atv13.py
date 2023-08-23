hast_aco   = int(input("Quantidade de hastes de aço compradas: "))
hast_cobre = int(input("Quantidade de hastes de cobre compradas: "))
hast_AI    = int(input("Quantidade de hastes de alumínio compradas: "))

precoAco   = 2.50
precoCobre = 4.00
precoAl    = 5.00

valorTotal = (hast_aco * precoAco) + (hast_cobre * precoCobre) + (hast_AI * precoAl)
qtdTotal = hast_aco + hast_cobre + hast_AI

if qtdTotal < 6:
    desconto = 0
elif 7 <= qtdTotal <= 15:
    desconto = valorTotal * 0.10
elif 16 <= qtdTotal <= 20:
    desconto = valorTotal * 0.15
else:
    desconto = valorTotal * 0.20

totalPago = valorTotal - desconto

print(f"Total a ser pago: R$ {totalPago:.2f}")