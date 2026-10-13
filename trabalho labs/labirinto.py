import heapq
from collections import deque

labirinto = [
    'I........#',
    '.#.##.##.#',
    '.#..##...#',
    '.....#.###',
    '.##.##...#',
    '#...#..#.#',
    '.##.####.#',
    '.......#..',
    '.#...#.##.',
    '.#.#.#...F'
]

def achar(lab, simbolo):
    for i, linha in enumerate(lab):
        if simbolo in linha:
            return (i, linha.index(simbolo))

inicio = achar(labirinto, 'I')
saida = achar(labirinto, 'F')

DIRECOES = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def livre(lab, i, j):
    dentro = 0 <= i < len(lab) and 0 <= j < len(lab[0])
    return dentro and lab[i][j] != '#'

def montar_grafo(lab):
    grafo = {}
    for i in range(len(lab)):
        for j in range(len(lab[0])):
            if not livre(lab, i, j):
                continue
            grafo[(i, j)] = []
            for di, dj in DIRECOES:
                if livre(lab, i + di, j + dj):
                    grafo[(i, j)].append((i + di, j + dj))
    return grafo

grafo = montar_grafo(labirinto)

def desenhar(lab, caminho):
    grade = [list(linha) for linha in lab]
    for i, j in caminho:
        if grade[i][j] == '.':
            grade[i][j] = '*'
    for linha in grade:
        print(''.join(linha))

def dfs(grafo, inicio, saida):
    visitados = set()
    
    def buscar(v):
        visitados.add(v)
        if v == saida:
            return [v]
        for w in grafo[v]:
            if w not in visitados:
                res = buscar(w)
                if res:
                    return [v] + res
        return None

    caminho = buscar(inicio)
    return caminho or [], len(visitados)

def bfs(grafo, inicio, saida):
    visitados = {inicio}
    fila = deque([inicio])
    pai = {inicio: None}
    
    while fila:
        v = fila.popleft()
        if v == saida:
            break
        for w in grafo[v]:
            if w not in visitados:
                visitados.add(w)
                pai[w] = v
                fila.append(w)
                
    if saida not in pai:
        return [], len(visitados)
        
    caminho = []
    atual = saida
    while atual is not None:
        caminho.append(atual)
        atual = pai[atual]
    caminho.reverse()
    
    return caminho, len(visitados)

def h(v, saida):
    return abs(v[0] - saida[0]) + abs(v[1] - saida[1])

def gulosa(grafo, inicio, saida):
    visitados = set()
    fronteira = [(h(inicio, saida), inicio)]
    pai = {inicio: None}
    
    while fronteira:
        _, v = heapq.heappop(fronteira)
        if v in visitados:
            continue
        visitados.add(v)
        
        if v == saida:
            break
            
        for w in grafo[v]:
            if w not in visitados:
                if w not in pai:
                    pai[w] = v
                heapq.heappush(fronteira, (h(w, saida), w))
                
    if saida not in pai:
        return [], len(visitados)
        
    caminho = []
    atual = saida
    while atual is not None:
        caminho.append(atual)
        atual = pai[atual]
    caminho.reverse()
    
    return caminho, len(visitados)

c_dfs, v_dfs = dfs(grafo, inicio, saida)
c_bfs, v_bfs = bfs(grafo, inicio, saida)
c_gulosa, v_gulosa = gulosa(grafo, inicio, saida)

print("--- DFS ---")
desenhar(labirinto, c_dfs)

print("\n--- BFS ---")
desenhar(labirinto, c_bfs)

print("\n--- GULOSA ---")
desenhar(labirinto, c_gulosa)

print("\n--- COMPARATIVO ---")
print("DFS: caminho =", len(c_dfs), "| visitados =", v_dfs)
print("BFS: caminho =", len(c_bfs), "| visitados =", v_bfs)
print("Gulosa: caminho =", len(c_gulosa), "| visitados =", v_gulosa)
