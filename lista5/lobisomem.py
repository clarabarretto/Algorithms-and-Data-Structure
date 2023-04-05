def dfs(vertice, visitados, grafo, contador):
  visitados.add(vertice)
  contador[0] += 1
  for vizinho in grafo[vertice]:
    if vizinho not in visitados:
      dfs(vizinho, visitados, grafo, contador)

primeiro_input = input().split()

n = int(primeiro_input[0])
m = int(primeiro_input[1])

grafo = [[] for i in range(n)]

for i in range(m):
  segundo_input = input().split()

  u = int(segundo_input[0])
  v = int(segundo_input[1])

  grafo[u-1].append(v-1)
  grafo[v-1].append(u-1)

resultado = ""

for i in range(n):
  visitados = set()
  contador = [0]
  dfs(i, visitados, grafo, contador)

  resultado += str(contador[0]) + " "

print(resultado.rstrip())