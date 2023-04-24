def bfs(grafo, u, b):
    visitados = []

    if u in grafo:
        user = grafo[u]
        for i in range(len(user)):
            visitados.append(user[i])

    alcance = b // 5.25

    for usuario in visitados:
        for i in grafo[usuario]:
            if i not in visitados and alcance > 0 and i != u:
                visitados.append(i)
                alcance -= 1

    return visitados


n = int(input())
u = int(input())
b = int(input())

grafo = {}

for i in range(n):
    q_usuarios = input().split()
    user_id = int(q_usuarios[0])
    seguidores = list(map(int, q_usuarios[2:]))
    grafo[user_id] = seguidores

output = bfs(grafo, u, b)
print(list(map(str, output)))
