numero_operacoes = int(input())


class tabelaHash:
    def __init__(self, tamanho=11):
        self.tamanho = tamanho
        self.tabela = [[] for i in range(self.tamanho)]

    def multiplicaCpf(self, lista):
        tamanho_lista = len(lista)
        for i in range(tamanho_lista):
            posicao = int(lista[i]) % self.tamanho
            if self.tabela[posicao] == []:
                self.tabela[posicao] = int(lista[i]) * 10
            else:
                self.tabela[posicao] += int(lista[i]) * 10
        return self.tabela

    def verificaSoma(self, lista, magic_number):
        print(lista)
        for i in range(len(lista)):
            if lista[i] == []:
                continue
            else:
                subtracao = int(magic_number) - lista[i]
                if subtracao in lista and subtracao != lista[i]:
                    print("UP Permission")
                    return
        print("NOT Permission")
        return

    def executaFuncoes(self, repeticoes, lista, magico):
        multiplicador = self.multiplicaCpf(lista)
        self.verificaSoma(multiplicador, magico)


for i in range(numero_operacoes):
    dado = input().split(" ")
    cpf = list(dado[0])
    magico = dado[1]
    tabela = tabelaHash()
    tabela.executaFuncoes(numero_operacoes, cpf, magico)
