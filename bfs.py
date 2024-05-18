
class BFS_ENV():
    def __init__(self, grafo: dict):
        self.grafo = grafo
        self.visited = set()
        self.parents = dict()

    def _reset(self):
        self.visited = set()
        self.parents = dict()

    def _BFS(self,  start_node):
        start_node = str(start_node)
        i = 1
        l = []
        l.append([start_node])
        self.parents[start_node] = None
        self.visited.add(start_node)
        while True:
            l.append([])
            for node in l[i-1]:
                for neighbor in self.grafo[node]:
                    if neighbor not in self.visited:
                        l[i].append(neighbor)
                        self.parents[neighbor] = node
                        self.visited.add(neighbor)
            if len(l[i]) == 0:
                return l
            i+=1
            
    def get_qtd_componentes_conexos(self):
        self._reset()
        cont = 0
        for i in self.grafo.keys():
            if i not in self.visited:
                cont+=1
                # print(f'Componentes conexos: {cont}')
                self._BFS(i)
        return cont

    def get_menor_caminho(self, start_node, end_node):
        start_node = str(start_node)
        end_node = str(end_node)
        self._reset()
        self._BFS(start_node)
        caminho = []
        if end_node in self.parents:
            no = end_node
            while no is not None:
                caminho.insert(0,no)
                no = self.parents[no]
        return caminho
    
    def get_cfg_mais_dificeis(self, end_node):
        end_node = str(end_node)
        self._reset()
        camadas = self._BFS(end_node)
        camada_mais_distante = camadas[-2]
        return camada_mais_distante
