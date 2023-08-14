altura_da_parede = int(input("digite a altura da parede: "))
largura = int (input("digite a largura da parede: "))
area_da_parede = altura_da_parede * largura

altura_do_azulejo = int (input("digite a altura do azulejo: "))
lagura_do_azulejo = int (input("digite a lagura do azulejo: "))
area_do_azulejo = altura_do_azulejo * lagura_do_azulejo
quant_azulejos_necessario = area_da_parede / area_do_azulejo

print(f"vai precisa de  { quant_azulejos_necessario} azulejo")