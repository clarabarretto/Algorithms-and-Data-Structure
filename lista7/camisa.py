n = int(input())
torcedores = list(map(int, input().split()))


def print_function(num):
    print(f"{num} torcedores podem ser fotografados.")
    return

if n == 1:
    print_function(torcedores[0])
elif n == 2:
    print_function(max(torcedores))
else:
    anterior = torcedores[0]
    atual = max(torcedores[0], torcedores[1])

    for i in range(2, n):
        anterior, atual = atual, max(anterior + torcedores[i], atual)

    print_function(atual)
