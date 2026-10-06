import random
import numpy as np
import time



if __name__ == '__main__':
    N = 1000
    BLOQUE = 100

    # Matriz 1000x1000 con enteros entre 0 y 9
    matriz1 = [[random.randint(0, 9) for _ in range(N)] for _ in range(N)]
    matriz2 = [[random.randint(0, 9) for _ in range(N)] for _ in range(N)]

    #Aplanarla antes de meter a array
    matriz_plana1 = np.array([x for fila in matriz1 for x in fila])
    matriz_plana2 = np.array([x for fila in matriz2 for x in fila])

    inicio = time.time()
    multiplicacion = matriz_plana1 * matriz_plana2

    suma_total = sum(multiplicacion)
    final = time.time()

    print("El tiempo es: ", final - inicio)
    print("La suma total es: ", suma_total)