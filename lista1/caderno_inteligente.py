folhas = input()

def pilha(caderno):
  tamanho_pilha = len(caderno)
  lista_F = []
  quantidade_F = 0
  quantidade_V = 0
  if tamanho_pilha == 0:
    print('Correto.')
    return
  for i, pagina in enumerate(caderno):
      if pagina == 'V':
        quantidade_V += 1
      if quantidade_V > quantidade_F:
        print(f'Incorreto, devido a capa na posição {i+1}.')
        return 
      if pagina == 'F':
        lista_F.append(i)
        quantidade_F += 1
  if(quantidade_F == quantidade_V):
      print('Correto.')
      return
  else:
    procurar_F = lista_F[quantidade_V]
    print(f'Incorreto, devido a capa na posição {procurar_F + 1}.')
    return 
  
pilha(folhas)
  