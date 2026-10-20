# Labirinto 10 × 10 — DFS, BFS e Busca Gulosa

## Descrição

Este projeto implementa um labirinto de 10 linhas por 10 colunas em Python e compara três algoritmos de busca: Busca em Profundidade (DFS), Busca em Largura (BFS) e Busca Gulosa.

O objetivo é encontrar um caminho da entrada (`I`) até a saída (`F`), mostrar o percurso de cada algoritmo e comparar o tamanho dos caminhos e a quantidade de casas visitadas.

## Representação do labirinto

```text
I........#
.#.##.##.#
.#..##...#
.....#.###
.##.##...#
##..#..#.#
.##.####.#
.......#..
.#..##.##.
.#.#.....F
```

**Legenda:**
- `I`: início
- `F`: saída
- `#`: parede (não pode ser atravessada)
- `.`: casa livre
- `*`: casa que faz parte do caminho encontrado (na saída do programa)

Os movimentos permitidos são para cima, direita, baixo e esquerda, sem diagonais.

## Algoritmos implementados

### DFS — Busca em Profundidade

Explora um caminho o mais profundamente possível antes de voltar e tentar outras alternativas. Usa recursão e um conjunto de casas visitadas. Não garante o menor caminho, pois depende da ordem em que os vizinhos são explorados.

### BFS — Busca em Largura

Explora as casas por níveis de distância a partir do início, utilizando uma fila. Como cada movimento tem o mesmo custo, garante o caminho com o menor número de movimentos. O programa guarda o predecessor (`pai`) de cada casa para reconstruir o caminho ao final.

### Busca Gulosa

Usa uma fila de prioridade e a distância de Manhattan como heurística:

`h = |linha_atual - linha_final| + |coluna_atual - coluna_final|`

Prioriza as casas que parecem estar mais próximas da saída, sem considerar o custo do caminho já percorrido. Por isso, não garante o menor caminho e pode ser desviada por paredes.

## Resultados

Resultados obtidos executando `python labirinto.py`:

| Algoritmo | Tamanho do caminho (casas) | Casas visitadas |
|---|---:|---:|
| DFS | 23 | 23 |
| BFS | 19 | 58 |
| Busca Gulosa | 23 | 23 |

O tamanho informado pelo programa conta as casas do caminho, incluindo início e saída. Portanto, os caminhos possuem respectivamente 22, 18 e 22 movimentos.

### Comparação dos resultados

A BFS encontrou o menor caminho, com 19 casas, mas visitou 58 casas durante a busca. A DFS encontrou um caminho de 23 casas, visitando 23. A Busca Gulosa também encontrou um caminho de 23 casas e visitou 23.

Neste labirinto, DFS e Busca Gulosa visitaram menos casas, mas seus caminhos ficaram 4 casas maiores que o da BFS. Assim, visitar menos casas durante a busca não significa necessariamente encontrar o percurso mais curto.

## Como executar

Requisito: Python 3 (sem bibliotecas externas).

1. Baixe ou clone este repositório.
2. Abra um terminal na pasta do projeto.
3. Execute:

```bash
python "labirinto(3).py"
```

O programa mostrará os três labirintos com os caminhos marcados por `*` e, ao final, a comparação entre os algoritmos.

## Estrutura do projeto

```text
.
├── labirinto(3).py
└── README.md
```

## Conclusão

O experimento demonstra que a BFS é a melhor opção quando a prioridade é garantir o menor caminho em um labirinto com movimentos de custo igual. A DFS pode encontrar uma saída rapidamente, mas não garante o menor percurso. A Busca Gulosa usa uma estimativa da distância até a saída para orientar a exploração, porém pode fazer escolhas inadequadas diante de obstáculos.
