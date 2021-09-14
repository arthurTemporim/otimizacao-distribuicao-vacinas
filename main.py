# -*- coding: utf-8 -*-
"""
Created on Sun Aug 22 12:00:08 2021

@author: pc-daniel
"""
import random
import bsb
import time, matplotlib  # , datetime
from itertools import combinations
import math


class Graph:
    def __init__(self):
        self.graph_dict = {}

    def addVertice(self, vertice, u, a):
        if vertice not in self.graph_dict:
            self.graph_dict[vertice] = {"uso": u, "armazenamento": a, "arestas": {}}

    def addAresta(self, v1, v2):
        try:
            if v1 != v2:
                self.graph_dict[v1]["arestas"][v2] = 1
                self.graph_dict[v2]["arestas"][v1] = 1
        except Exception as e:
            print(f"Error: Problema na adição de aresta: {e}")


# Função que identifica subgrafos a partir de um vértice
def identificaSub(G, v, sub):
    l = list(G.graph_dict[v]["arestas"].keys())
    # Percorre as arestas de um vértice
    for i in l:
        # Se o vértice não está no subconjunto, ele é adicionado
        if v not in sub:
            sub.append(v)
        # Se o V destino da aresta não está no subconjunto, ele é adicionado
        if i not in sub:
            sub.append(i)
            identificaSub(G, i, sub)
    return sub


# Função para identificar vértices isolados que não possuem arestas
def isolados(l, sub):
    for i in sub:
        for j in i:
            if j in l:
                l.remove(j)
    return l


# Função que retorna verdadeiro caso seja um grafo conexo ou a lista de subgrafos
def eh_conexo(G):
    subgrafos = []  # lista de grafos isolados
    l = list(G.graph_dict.keys())
    # Percorre o Grafo chamando a função que identifica subgrafos a partir de um vértice
    for v in l:
        sub = identificaSub(G, v, [])
        sub = sorted(sub)
        if len(sub) > 0 and sub not in subgrafos:
            subgrafos.append(sub)
    iso = isolados(l, subgrafos)
    for i in iso:
        subgrafos.append([i])
    l = list(G.graph_dict.keys())
    # Retorna verdadeiro se a lista de todos os vértices de um grafo é um dos subconjuntos,
    # retorna a lista de subconjuntos caso contrário
    if l in subgrafos:
        return True
    else:
        return subgrafos


def conecta_grafo(G):
    subgrafo = eh_conexo(G)
    # Verifica se o grafo já é conectado:
    # Se não cria uma conexão do 1º elemento de cada subgrafo para o 1º elemento do próximo subgrafo
    if subgrafo == True:
        # print("Ja conectado")
        pass
    else:
        for i in range(0, (len(subgrafo) - 1)):
            G.addAresta(subgrafo[i][0], subgrafo[i + 1][0])
        # print("Grafo foi conectado")


# Soma o custo de armazenamento dos vértices em v_linha
def custo_armazenamento_v_linha(G, v_linha):
    soma = 0
    for i in v_linha:
        soma = soma + G.graph_dict[i]["armazenamento"]
    return soma


# Algoritmo de busca em largura
def BFS(G, v, v_linha):
    # Se v pertence a v_linha, retorne a distancia 1
    if v in v_linha:
        return 1
    # Armazenando o tamanho do grafo
    t = len(G.graph_dict.keys())
    atuais = [v]
    proximos = []
    percorridos = [v]
    dist = 0
    # Em um loop do tamanho do grafo:
    for i in range(t):
        # Percorra todas as vértices na lista atuais
        for j in atuais:
            # Percorra todas as arestas de cada vértice na lista atuais
            for h in G.graph_dict[j]["arestas"].keys():
                # Se o vértice ainda não foi percorrido, adiciona ele nos próximos a serem percorridos
                if h not in percorridos:
                    # Se chegou em v_linha, retorne a distancia
                    if h in v_linha:
                        dist = dist + 1
                        return dist
                    proximos.append(h)
                    percorridos.append(h)
        # No final de cada ciclo de distancia, renova a lista de atuais com os próximos e zera os próximos
        dist = dist + 1
        atuais = proximos
        proximos = []


# Calcula a soma das menores distancias de cada vertice em G para v_linha
def soma_menor_distancia(G, v_linha):
    soma = 0
    for v in list(G.graph_dict.keys()):
        soma = soma + BFS(G, v, v_linha) * G.graph_dict[v]["uso"]
    return soma


def SR6(G, v_linha):
    # Calcula a soma do custo de armazenamento
    soma1 = custo_armazenamento_v_linha(G, v_linha)
    # Calcula a soma das menores distancias multiplicadas pelo uso
    soma2 = soma_menor_distancia(G, v_linha)
    # print(soma1,  soma2)
    # return (soma1 + soma2) <= k
    return soma1 + soma2


def reduz_grafo(G, n):
    # De 0 até n, verifica se cada vértice possui uma aresta maior que n, se sim remove
    for i in range(n):
        for a in list(G.graph_dict[i]["arestas"].keys()):
            if a >= n:
                del G.graph_dict[i]["arestas"][a]
    tam = len(list(G.graph_dict.keys()))
    # Remove os vértices maiores que n
    for i in range(n, tam):
        del G.graph_dict[i]


# Função que identifica o melhor V' utilizando força bruta
def melhor_v_linha(G, quantidade_v_linha):
    # Cria a combinação de todos os V' possíveis em G
    comb = combinations(list(G.graph_dict.keys()), quantidade_v_linha)
    k = float("inf")
    v_linha = []
    # Percorre toda a combinação calculando o SR6 e salvando o menor resultado
    for i in list(comb):
        resultado = SR6(G, i)
        if k > resultado:
            k = resultado
            v_linha = i
    return v_linha, k


def melhor_v_linha_aproximado_otimizado(G, quantidade_v_linha):
    t = len(G.graph_dict.keys())
    r = int(t / 2)
    l = []
    for i in G.graph_dict.keys():
        l.append((i, len(G.graph_dict[i]["arestas"].keys())))
    s = []
    for e in sorted(l, key=lambda x: x[1], reverse=True)[:r]:
        s.append(e[0])
    # Cria a combinação de todos os V' possíveis em G
    comb = combinations(s, quantidade_v_linha)
    k = float("inf")
    v_linha = []
    # Percorre toda a combinação calculando o SR6 e salvando o menor resultado
    for i in list(comb):
        resultado = SR6(G, i)
        if k > resultado:
            k = resultado
            v_linha = i
    return v_linha, k


def escolhe_nos_aleatoriamente(G, quantidade_v_linha, lista_combinacao, contador=3):
    lista_nos = list(G.graph_dict.keys())
    lista_combinacoes = list()
    for i in range(quantidade_v_linha):
        no_escolhido = random.choice(lista_nos)
        lista_combinacoes.append(no_escolhido)
        lista_nos.remove(no_escolhido)
    if lista_combinacoes in lista_combinacao and contador > 0:
        escolhe_nos_aleatoriamente(
            G, quantidade_v_linha, lista_combinacao, contador - 1
        )
    return tuple(lista_combinacoes)


def escolhe_no(lista_nos=None):
    no_escolhido = random.choice(lista_nos)
    lista_nos.remove(no_escolhido)
    return no_escolhido, lista_nos


def atualiza_lista_nos(G, melhores_nos=None):
    lista_nos = list(G.graph_dict.keys())
    for no in lista_nos:
        if no in melhores_nos:
            lista_nos.remove(no)
    return lista_nos


def calcula_temperatura(temperatura=None, contador=None, lista_resultados=None):
    custo = lista_resultados[1] - lista_resultados[0]
    temperatura -= contador
    temp = False
    if custo != 0 and temperatura != 1:
        temp = not (random.uniform(0, 1) < math.exp(-custo / temperatura))
    nova_lista_resultados = lista_resultados[1:]
    return temp, nova_lista_resultados, temperatura


def melhor_v_linha_aproximado(
    G=None, quantidade_v_linha=32, iteracoes=32, temperatura=10
):
    lista_nos = list(G.graph_dict.keys())
    melhores_nos = list()
    for i in range(quantidade_v_linha):
        k = float("inf")
        lista_resultados = list()
        if iteracoes > len(lista_nos):
            iteracoes = len(lista_nos) - 1
        for j in range(iteracoes):
            no_escolhido, nova_lista_nos = escolhe_no(lista_nos)
            lista_nos = nova_lista_nos.copy()
            melhores_nos.append(no_escolhido)
            resultado = SR6(G, melhores_nos)
            if k >= resultado:
                k = resultado
                melhor_no = no_escolhido
            lista_resultados.append(resultado)
            if len(lista_resultados) > 1:
                temp, lista_resultados, temperatura = calcula_temperatura(
                    temperatura, iteracoes, lista_resultados
                )
                if k >= resultado:
                    k = resultado
                    melhor_no = no_escolhido
                elif temp:
                    k = resultado
                    melhor_no = no_escolhido

            melhores_nos.pop()
        if melhor_no in melhores_nos:
            return melhores_nos, k
        melhores_nos.append(melhor_no)
        lista_nos = atualiza_lista_nos(G, melhores_nos)
    return melhores_nos, k


def interface_menu():
    print(
        "Algoritmo para solucionar o problema SR6 - Adaptado para distribuição de vacinas\n"
    )
    print(
        "Este algoritmo se baseia no grafo das regiões administrativas do DF,\n"
        "por favor insira um valor de 1 até 32\n"
        "para representar a quantidade de vértices ou -1 para encerrar:\n"
    )
    x = input()
    if x == "":
        x = 32
    else:
        x = int(x)
    while x != -1:
        if x != -1 and x < 33:
            print("Digite a quantidade de postos de distribuição desejado:")
            n = int(input())
            if n > x or n < 1:
                print("Quantidade de postos inválida!")
                break
            # Cria um grafo G
            G = Graph()
            # Adiciona as vértices e arestas de brasília
            bsb.cria_bsb(G)
            if x < 32:
                # Reduz o grafo para o tamanho x
                reduz_grafo(G, x)
                # Conecta os vértices isolados no grafo
                conecta_grafo(G)
            print("Grafo Criado.\n")

            if n >= 5:
                print("Deseja mesmo executar a solução FORÇA BRUTA? (s/n)")
                valida_forca_bruta = input()
                if valida_forca_bruta == "s":
                    print("SOLUÇÃO FORÇA BRUTA:")
                    inicio = time.time()
                    v_linha, k = melhor_v_linha(G, n)
                    fim = time.time()
                    print("Melhor V':", v_linha, " Melhor K: ", k)
                    print("Tempo de execução em segundos:", fim - inicio)
                    print("\n")
            else:
                print("SOLUÇÃO FORÇA BRUTA:")
                inicio = time.time()
                v_linha, k = melhor_v_linha(G, n)
                fim = time.time()
                print("Melhor V':", v_linha, " Melhor K: ", k)
                print("Tempo de execução em segundos:", fim - inicio)
                print("\n")

            print("SOLUÇÃO APROXIMADA UTILIZANDO META-HEURÍSTICA SIMULATED ANNEALING:")
            inicio = time.time()
            v_linha, k = melhor_v_linha_aproximado(G, n)
            fim = time.time()
            print("Melhor V':", v_linha, " Melhor K: ", k)
            print("Tempo de execução em segundos:", fim - inicio)
            print("\n")

            print("SOLUÇÃO OTIMIZADA:")
            inicio = time.time()
            v_linha, k = melhor_v_linha_aproximado_otimizado(G, n)
            fim = time.time()
            print("Melhor V':", v_linha, " Melhor K: ", k)
            print("Tempo de execução em segundos:", fim - inicio)
            print("\n\n")


if __name__ == "__main__":
    interface_menu()
