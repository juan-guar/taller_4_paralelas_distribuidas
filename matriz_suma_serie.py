import random
import time


if __name__ == '__main__':
    N = 1000
    suma = 0

    matriz = [[random.randint(0, 9) for _ in range(N)] for _ in range(N)]

    matriz_plana = [x for fila in matriz for x in fila]

    time_inicio = time.time()
    for i in range(len(matriz_plana)):
        suma += matriz_plana[i]


    timen_final = time.time()
    print("La suma total de la matriz es: ", suma)
    print("El tiempo de ejecucion fue: ", timen_final - time_inicio)