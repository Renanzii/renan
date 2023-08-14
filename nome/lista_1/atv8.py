ponto_de_inicio = 2
velocidade_de_inicio = 3
aceleração = 10
tempo = int (input("Digiteo tempo : "))
distancia_percorrida = ponto_de_inicio + velocidade_de_inicio * tempo + 1/2 * aceleração * tempo ** 2

print(f" A distancia percorrida {distancia_percorrida}")