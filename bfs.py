import numpy as np

class BFS_ENV():
    def __init__(self, grafo: dict):
        self.grafo = grafo
        self.visited = set()

    def _BFS(self,  start_node: str):
        i = 1
        l = []
        l.append([start_node])
        self.visited.add(start_node)
        while True:
            l.append([])
            for node in l[i-1]:
                for neighbor in self.grafo[node]:
                    neighbor_string = str(neighbor)
                    if neighbor_string not in self.visited:
                        l[i].append(neighbor_string)
                        self.visited.add(neighbor_string)
            if len(l[i]) == 0:
                return l
            i+=1
            
    def BFS(self):
        cont = 1
        for i in self.grafo.keys():
            print(f'\rComponentes conexos: {cont}', end='')
            if i not in self.visited:
                cont+=1
                self._BFS(i)
        return cont