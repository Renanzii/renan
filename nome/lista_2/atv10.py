salario_bruto = float(input("Informe o salário bruto: "))

if salario_bruto <= 1903.98:
    impost = 0
    deducao = 0
elif salario_bruto <= 2826.65:
    impost = 0.075
    deducao = 142.80
elif salario_bruto <= 3751.05:
    impost = 0.15
    deducao = 548.82
elif salario_bruto <= 4664.68:
    impost = 0.225
    deducao = 636.13
else:
    impost = 0.275
    deducao = 869.36

desconto_irrf = (salario_bruto * impost) - deducao
salario_liquido = salario_bruto - desconto_irrf

print(f"Salário bruto: R$ {salario_bruto:.2f}")
print(f"Desconto do IRRF: R$ {desconto_irrf:.2f}")
print(f"Salário líquido: R$ {salario_liquido:.2f}")