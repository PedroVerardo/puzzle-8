
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
                    if neighbor not in self.visited:
                        l[i].append(neighbor)
                        self.visited.add(neighbor)
            if len(l[i]) == 0:
                return l
            i+=1
            
    def BFS(self):
        cont = 0
        for i in self.grafo.keys():
            if i not in self.visited:
                cont+=1
                print(f'Componentes conexos: {cont}')
                self._BFS(i)
        return cont