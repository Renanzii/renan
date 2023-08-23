n = int(input("quantos numeros de sequancia de fibonnaci vc quer :"))

fibonacci = [0,1]

for i in range(2,n):
    proximo_num = fibonacci[i - 1] + fibonacci[i - 2]
    fibonacci.append(proximo_num)

print("os numeros", n,"numeros da sequencia de fibonacci sao:", fibonacci)
