import random

class Fila:
    def __init__(self):
        self.itens = []
    def enfileirar(self, item):
        self.itens.append(item)
    def desenfileirar(self):
        if not self.vazia():
            return self.itens.pop(0)
        raise IndexError("Fila vazia")
    def vazia(self):
        return len(self.itens) == 0
    def mostrar(self):
        return self.itens

class Pilha:
    def __init__(self):
        self.itens = []
    def empilhar(self, item):
        self.itens.append(item)
    def desempilhar(self):
        if not self.vazia():
            return self.itens.pop()
        raise IndexError("Pilha vazia")
    def vazia(self):
        return len(self.itens) == 0
    def mostrar(self):
        return self.itens

def busca_sequencial(lista, alvo):
    for i, item in enumerate(lista):
        if item["nome"] == alvo:
            return i, item
    return -1, None

def busca_binaria(lista, alvo):
    esquerda, direita = 0, len(lista) - 1
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if lista[meio]["nome"] == alvo:
            return meio, lista[meio]
        elif lista[meio]["nome"] < alvo:
            esquerda = meio + 1
        else:
            direita = meio - 1
    return -1, None

def merge_sort(lista, chave):
    if len(lista) <= 1:
        return lista
    meio = len(lista) // 2
    esquerda = merge_sort(lista[:meio], chave)
    direita = merge_sort(lista[meio:], chave)
    return merge(esquerda, direita, chave)

def merge(esquerda, direita, chave):
    resultado = []
    i = j = 0
    while i < len(esquerda) and j < len(direita):
        if esquerda[i][chave] <= direita[j][chave]:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1
    resultado.extend(esquerda[i:])
    resultado.extend(direita[j:])
    return resultado

def quick_sort(lista, chave):
    if len(lista) <= 1:
        return lista
    pivo = lista[len(lista) // 2][chave]
    menores = [x for x in lista if x[chave] < pivo]
    iguais = [x for x in lista if x[chave] == pivo]
    maiores = [x for x in lista if x[chave] > pivo]
    return quick_sort(menores, chave) + iguais + quick_sort(maiores, chave)

def simular_consumo(qtd_dias=10):
    nomes = ["ReagenteA", "ReagenteB", "ReagenteC", "ReagenteD"]
    fila = Fila()
    pilha = Pilha()
    for dia in range(1, qtd_dias + 1):
        consumo = {
            "nome": random.choice(nomes),
            "quantidade": random.randint(1, 50),
            "validade": random.randint(1, 365),
            "dia": dia
        }
        fila.enfileirar(consumo)
        pilha.empilhar(consumo)
    return fila, pilha

def main():
    try:
        fila, pilha = simular_consumo()
        registros = fila.mostrar()

        print("Consumo (Fila - ordem cronológica):")
        for item in registros:
            print(item)

        print("\nConsumo (Pilha - ordem inversa):")
        for item in pilha.mostrar()[::-1]:
            print(item)

        print("\nBusca Sequencial:")
        print(busca_sequencial(registros, "ReagenteB"))

        print("\nOrdenação Merge Sort por quantidade:")
        ordenado_merge = merge_sort(registros, "quantidade")
        for item in ordenado_merge:
            print(item)

        print("\nOrdenação Quick Sort por validade:")
        ordenado_quick = quick_sort(registros, "validade")
        for item in ordenado_quick:
            print(item)

        print("\nBusca Binária (lista ordenada por nome):")
        registros_ordenados_nome = merge_sort(registros, "nome")
        print(busca_binaria(registros_ordenados_nome, "ReagenteC"))

    except Exception as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    main()
