solicitacoes = input().split(",")
solicitacoesOrd = sorted(solicitacoes)
novaSolicitacao = input()


def novaLocacao(pilha, codigo):
    tamanhoPilha = len(pilha)

    if codigo < pilha[0]:
        pilha.insert(0, codigo)

    elif codigo > pilha[tamanhoPilha - 1]:
        pilha.insert(tamanhoPilha, codigo)

    else:
        for i in range(tamanhoPilha):
            if codigo > pilha[i] and codigo < pilha[i + 1]:
                pilha.insert(i + 1, codigo)
    return pilha


if solicitacoes == solicitacoesOrd:
    resposta = novaLocacao(solicitacoes, novaSolicitacao)
    print(resposta)
else:
    print("A pilha está um caos.")
