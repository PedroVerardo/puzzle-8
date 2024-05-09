import numpy as np

visited = set()

def BFS(grafo: dict,  start_node: str):
    i = 1
    l = []
    visited = set()
    l.append([start_node])
    visited.add(start_node)
    while True:
        l.append([])
        for node in l[i-1]:
            for neighbor in grafo[node]:
                neighbor_string = np.array2string(neighbor, separator=',')
                if neighbor_string not in visited:
                    l[i].append(neighbor_string)
        if len(l[i]) == 0:
            return l
        
def BFS2(grafo: dict):
    for i in grafo.keys():
        if i not in visited:
            BFS(grafo, i)