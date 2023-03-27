lista_folha = None

def heapify(seq, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and seq[l] > seq[largest]:
        largest = l
    if r < n and seq[r] > seq[largest]:
        largest = r
    if largest != i:
        seq[i], seq[largest] = seq[largest], seq[i]
        heapify(seq, n, largest)

def heapSort(seq):
    global lista_folha
    n = len(seq)
    lista_folha = n // 2
    for i in range(lista_folha - 1, -1, -1):
        heapify(seq, n, i)

def minimo(seq, f):
  find = seq[f]
  for i in range(f, len(seq)):
    if seq[i] < find:
      find = seq[i]
  return find

def jogo(seq, constante):
    heapSort(seq)
    rodadas = 0
    while seq:
        maior = seq[0]
        k = maior - abs(minimo(seq, lista_folha) * constante)
        if k > 0:
            seq.extend([k])
            heapSort(seq)
        seq.remove(maior)
        heapSort(seq)
        rodadas += 1
    return rodadas

seq = list(map(int, input().split()))
constante = int(input())

rodadas = jogo(seq, constante)

print(f"{rodadas} rodadas, partindo para a próxima!")
