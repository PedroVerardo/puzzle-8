import gera_grafo_estados
from bfs import BFS_ENV

grafo = gera_grafo_estados.gera_grafo()

bfs_env = BFS_ENV(grafo)

print(bfs_env.BFS())