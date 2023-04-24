fim = False


class No:
    def __init__(self, valor, anterior, proximo):
        self.valor = valor
        self.anterior = anterior
        self.proximo = proximo


class Lista:
    def __init__(self):
        self.comeco = None
        self.fim = None

    def comandos(self, acao, entrada):
        if acao == "REM":
            self.remove(entrada[1])
        if acao == "ADD":
            self.insere(entrada[1])
        if acao == "FIND":
            self.procura(entrada[1])
        if acao == "EXIB":
            self.exibe()
        if acao == "END":
            return True
        return False

    def remove(self, dado):
        no_atual = self.comeco
        while no_atual is not None:
            if no_atual.valor == dado:
                if no_atual.anterior is not None:
                    no_atual.anterior.proximo = no_atual.proximo
                else:
                    self.comeco = no_atual.proximo

                if no_atual.proximo is not None:
                    no_atual.proximo.anterior = no_atual.anterior
                else:
                    self.fim = no_atual.anterior
                return
            no_atual = no_atual.proximo

    def insere(self, valor):
        novo_no = No(valor, None, None)
        if self.comeco is None:
            self.comeco = novo_no
            self.fim = novo_no
        else:
            novo_no.anterior = self.fim
            novo_no.proximo = None
            self.fim.proximo = novo_no
            self.fim = novo_no

    def exibe(self):
        no_atual = self.fim
        while no_atual is not None:
            print(no_atual.valor)
            no_atual = no_atual.anterior

    def procura(self, valor):
        no_atual = self.comeco
        achou = False
        while no_atual != None:
            if no_atual.valor == valor:
                achou = True
                break
            no_atual = no_atual.proximo
        if achou:
            self.remove(valor)
            self.insere(valor)


lista = Lista()
while not fim:
    input_comandos = input().split(" ")
    fim = lista.comandos(input_comandos[0], input_comandos)
