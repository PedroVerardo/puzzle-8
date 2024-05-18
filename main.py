import gera_grafo_estados
from bfs import BFS_ENV

print("Gerando grafo de estados.")
grafo = gera_grafo_estados.gera_grafo()
print("Grafo de estados gerado")


bfs_env = BFS_ENV(grafo)

print(bfs_env.BFS())
