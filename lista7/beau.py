def subgrupos(n):
    subgrupos_validos = []
    subgrupo_atual = []

    def gerar_subgrupos(soma_atual, num_atual):
        if soma_atual == n:
            subgrupos_validos.append(subgrupo_atual[:])
        elif soma_atual < n and len(subgrupo_atual) < n:
            for i in range(num_atual, n - soma_atual + 1):
                subgrupo_atual.append(i)
                gerar_subgrupos(soma_atual + i, i)
                subgrupo_atual.pop()

    gerar_subgrupos(0, 1)

    print(f"Uma sessão com {n} pessoas pode ter sua audiência nos seguintes subgrupos:")
    for subgrupo in subgrupos_validos:
        print(subgrupo)


n = int(input())
subgrupos(n)
