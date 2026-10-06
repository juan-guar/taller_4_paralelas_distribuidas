from multiprocessing import Process, Lock, Value, RawArray
import time
import numpy as np


def sumar_parte(buffer_compartido, N, suma_compartida, inicio, fin, lock):
    matriz = np.frombuffer(buffer_compartido, dtype=np.int8).reshape(N, N)
    # dtype=np.int64 para evitar desbordes en la suma
    suma_local = matriz[inicio:fin].sum(dtype=np.int64)

    with lock:
        suma_compartida.value += int(suma_local)


if __name__ == '__main__':
    N = 10000
    BLOQUE = 1000  # filas por proceso

    # Reserva de memoria compartida
    buffer = RawArray('b', N * N)

    # Para no crear una matriz nueva.
    # Un objeto NumPy que usa la misma memoria que otro objeto, sin copiar los datos.
    matriz = np.frombuffer(buffer, dtype=np.int8).reshape(N, N)

    matriz[:] = np.random.randint(0, 10, size=(N, N), dtype=np.int8)


    suma_compartida = Value('q', 0)
    lock = Lock()

    time_inicio = time.time()
    procesos = []

    for inicio in range(0, N, BLOQUE):
        fin = min(inicio + BLOQUE, N)
        procesos.append(Process(
            target=sumar_parte,
            args=(buffer, N, suma_compartida, inicio, fin, lock)
        ))

    for p in procesos:
        p.start()
    for p in procesos:
        p.join()

    time_final = time.time()
    print("La suma total de la matriz es:", suma_compartida.value)
    print("El tiempo de ejecucion fue:", time_final - time_inicio)