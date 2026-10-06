from multiprocessing import Process, Lock, Array, Value
import random
import time


def sumar_parte(matriz_compartida, suma_compartida, inicio, fin, lock, n):
    suma_local = 0
    for i in range(inicio, fin):
        base = i * n
        for j in range(n):
            suma_local += matriz_compartida[j + base]
    with lock:
        suma_compartida.value += suma_local


if __name__ == '__main__':
    N = 1000
    BLOQUE = 100


    # Matriz 1000x1000 con enteros entre 0 y 9
    matriz = [[random.randint(0, 9) for _ in range(N)] for _ in range(N)]

    #Aplanarla antes de meter a array
    matriz_plana = [x for fila in matriz for x in fila]
    matriz_compartida = Array('i', matriz_plana)

    # Usamos q para evitar desbordes
    suma_compartida = Value('q', 0)

    lock = Lock()

    time_inicio = time.time()
    procesos = []

    for inicio in range(0, N, BLOQUE):
        fin = min(inicio + BLOQUE, N)
        procesos.append(Process(target=sumar_parte,args=(matriz_compartida, suma_compartida,
                inicio, fin, lock, N)))

    for proceso in procesos:
        proceso.start()

    for proceso in procesos:
        proceso.join()

    timen_final = time.time()
    print("La suma total de la matriz es: ", suma_compartida.value)
    print("El tiempo de ejecucion fue: ", timen_final - time_inicio)