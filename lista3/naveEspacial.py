lista_dados = []
memoria = int(input())
quantidade_comandos = int(input())

def posicaoLivre(espaco):
    for i, valor in enumerate(espaco):
        if valor is None:
            return i
    return None

def adicionar(espaco, dado):
    posicao = dado % memoria
    if espaco[posicao] is None:
      espaco[posicao] = dado
      print(f"E: {posicao}")
    else:
      posicao_nova = (posicao + 1) % memoria
      while posicao_nova != posicao:
          if espaco[posicao_nova] is None:
              espaco[posicao_nova] = dado
              print(f"E: {posicao_nova}")
              return
          posicao_nova = (posicao_nova + 1) % memoria
      print("Toda memoria utilizada")

def consulta_dado(espaco, dado):
    tamanho_espaco = len(espaco)
    posicao = dado % memoria
    if espaco[posicao] is None:
        print("NE")
    elif espaco[posicao] == dado:
        print(f"E: {posicao}")
    else:
        for i in range(tamanho_espaco):
            if espaco[i] == dado:
                print(f"E: {i}")
                return
        print("NE")

def consulta_memoria(espaco, posicao):
    if espaco[posicao] is None:
        print("D")
    else:
        print(f"A: {espaco[posicao]}")

for i in range(memoria):
    lista_dados.append(None)

for i in range(quantidade_comandos):
    entrada = input().split(' ')
    dado = int(entrada[1])
    if entrada[0] == "ADD":
        adicionar(lista_dados, dado)
    elif entrada[0] == "SCH":
        consulta_dado(lista_dados, dado)
    elif entrada[0] == "CAP":
        consulta_memoria(lista_dados, dado )