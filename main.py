import numpy as np
import random
from collections import deque
import base64
import time

def gera_grafo_aleatorio():
    numeros = list(range(1,10))

    random.shuffle(numeros)

    result = numeros[:9]

    arr = np.array(result).reshape(3, 3)


    return arr

def swap(estado_jogo: np.array, x2: int, y2: int) -> np.array:
    estado_jogo2 = estado_jogo.copy()
    x1, y1 = np.where(estado_jogo == 9)

    x1, y1 = x1[0], y1[0]

    temp = estado_jogo2[x1, y1]
    estado_jogo2[x1, y1] = estado_jogo2[x2, y2]
    estado_jogo2[x2, y2] = temp

    return estado_jogo2

def get_possible_moves(estado_jogo: np.array) -> list:
    x, y = np.where(estado_jogo == 9)

    x,y = x[0],y[0]

    possible_moves = []
    if x > 0:
        possible_moves.append(swap(estado_jogo, x-1, y))
    if x < 2:
        possible_moves.append(swap(estado_jogo, x+1, y))
    if y > 0:
        possible_moves.append(swap(estado_jogo, x, y-1))
    if y < 2:
        possible_moves.append(swap(estado_jogo, x, y+1))

    return possible_moves

def is_final_state(estado_jogo: np.array) -> bool:
    ''' Não possui uso necessário ainda'''
    return np.array_equal(estado_jogo, np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

def add_state_to_queue(estado_jogo: np.array, fila: deque, conjunto: set) -> None:
    estado_string = np.array2string(estado_jogo, separator=', ')
    if estado_string not in conjunto:
        fila.append(estado_jogo)
        conjunto.add(estado_string)

def estado2string(estado_jogo: np.array) -> str:
    return 

def gera_grafo_estados(estado_jogo: np.array) -> dict:
    estados = {}
    fila = deque()
    conjunto = set()
    start_time = time.time()
    fila.append(estado_jogo)
    edges = 0
    while fila:
        elapsed_time = time.time() - start_time
        estado:np.array = fila.popleft()

        possible_moves = get_possible_moves(estado)

        estado_string = np.array2string(estado, separator=', ')

        estados[estado_string] = possible_moves
        edges += len(possible_moves)

        for move in possible_moves:
            add_state_to_queue(move, fila, conjunto)

    end_time = time.time()    
    with open("results.txt", 'w') as f:
        f.write(f'Tempo de execucao: {end_time - start_time} segundos\n')
        f.write(f'Numero de estados: {len(estados)}\n')
        f.write(f'Numero de arestas: {edges}\n')
    return estados
    

if __name__ == '__main__':
    estado_ini = gera_grafo_aleatorio()

    grafo = gera_grafo_estados(estado_ini)