import time
import random



if __name__ == '__main__':
    N = 1000
    BLOQUE = 100
    multiplicacion = 0

    # Matriz 1000x1000 con enteros entre 0 y 9
    matriz1 = [[random.randint(0, 9) for _ in range(N)] for _ in range(N)]
    matriz2 = [[random.randint(0, 9) for _ in range(N)] for _ in range(N)]

    #Aplanarla antes de meter a array
    matriz_plana1 = [x for fila in matriz1 for x in fila]
    matriz_plana2 = [x for fila in matriz2 for x in fila]

    inicio = time.time()

    for i in range(0, len(matriz_plana1)):
        multiplicacion += matriz_plana1[i] * matriz_plana2[i]

    final = time.time()

    print("El tiempo es: ", final - inicio)
    print("La suma total es: ", multiplicacion)