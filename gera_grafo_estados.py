
def gera_estados_recursivo(n):
    #caso base
    if n == 1:
        return [[1]]
    
    #caso recursivo
    A = gera_estados_recursivo(n-1)
    B = []
    for i in range(n):
        for _a in A:
            _b = _a[:i]+[n]+_a[i:]
            B.append(_b)
    return B


def get_vizinhos(no,vazio=9):
    i = no.index(vazio)
    nos_vizinhos = []

    # buraco não está em baixo
    if i < 6:
        vizinho = no.copy()
        vizinho[i] = no[i+3]
        vizinho[i+3] = no[i]
        nos_vizinhos.append(str(vizinho))

    # buraco não está em cima
    if i > 2:
        vizinho = no.copy()
        vizinho[i] = no[i-3]
        vizinho[i-3] = no[i]
        nos_vizinhos.append(str(vizinho))

    # buraco não está na esquerda
    if i%3 > 0:
        vizinho = no.copy()
        vizinho[i] = no[i-1]
        vizinho[i-1] = no[i]
        nos_vizinhos.append(str(vizinho))

    # buraco não está na direita
    if i%3 < 2:
        vizinho = no.copy()
        vizinho[i] = no[i+1]
        vizinho[i+1] = no[i]
        nos_vizinhos.append(str(vizinho))

    return nos_vizinhos

def str2list(no_str):
    _s = no_str[1:-1]
    _s = _s.split(",")
    no_list = [int(x) for x in _s]
    return no_list


def imprime_estado(no,vazio=9):
    if type(no) == str:
        no = str2list(no)
    print("-"*9)
    for i in range(3):
        _s = "|"
        # print("|")
        for el in no[3*i:3*i+3]:
            if el != vazio:
                _s += " %d"%el
            else:
                _s += "  "
        _s += " |"
        print(_s)
    print("-"*9)


def gera_grafo():
    estados = gera_estados_recursivo(9)
    
    grafo = dict()
    for no in estados:
        grafo[str(no)] = get_vizinhos(no)
    
    return grafo


if __name__ == "__main__":
    grafo = gera_grafo()

    n = len(grafo)
    m = 0
    for no in grafo:
        m+=len(grafo[no])
    
    no = list(grafo.keys())[n//2]
    
    imprime_estado(no)
    for viz in grafo[no]:
        imprime_estado(viz)
    
    print(f"{n=}\n{m=}")
