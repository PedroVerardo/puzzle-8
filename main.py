from state_graph import gera_grafo_estados
from state_graph import gera_grafo_aleatorio
from bfs import BFS_ENV

estado_ini = gera_grafo_aleatorio()
grafo = gera_grafo_estados(estado_ini)

bfs_env = BFS_ENV(grafo)

print(bfs_env.BFS())