# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 16:26:07 2021

@author: danie
"""


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
        except (KeyError):
            pass


G = Graph()

vertices = [
    "Plano Piloto",
    "Gama",
    "Taguatinga",
    "Brazlândia",
    "Sobradinho",
    "Planaltina",
    "Paranoá",
    "Núcleo Bandeirante",
    "Ceilândia",
    "Guará",
    "Cruzeiro",
    "Samambaia",
    "Santa Maria",
    "São Sebastião",
    "Recanto das Emas",
    "Lago Sul",
    "Riacho Fundo",
    "Lago Norte",
    "Candangolândia",
    "Águas Claras",
    "Riacho Fundo 2",
    "Sudoeste/Octogonal",
    "Varjão",
    "Park Way",
    "Estrutural/Scia",
    "Sobradinho II",
    "Jardim Botânico",
    "Itapoã",
    "SIA",
    "Vicente Pires",
    "Fercal",
    "Sol Nascente/Pôr do Sol",
    "Arniqueira",
]


def cria_bsb(G):
    # Vértices
    # for i in range(0, 33):
    #    G.addVertice(i, 1, 1)

    G.addVertice(0, 217, 9238)
    G.addVertice(1, 132, 3454)
    G.addVertice(2, 210, 3908)
    G.addVertice(3, 53, 1)
    G.addVertice(4, 69, 3258)
    G.addVertice(5, 177, 1)
    G.addVertice(6, 65, 1)
    G.addVertice(7, 24, 4027)
    G.addVertice(8, 349, 3769)
    G.addVertice(9, 133, 5292)
    G.addVertice(10, 31, 6575)
    G.addVertice(11, 231, 3724)
    G.addVertice(12, 126, 2937)
    G.addVertice(13, 92, 1)
    G.addVertice(14, 131, 1)
    G.addVertice(15, 29, 1)
    G.addVertice(16, 42, 3868)
    G.addVertice(17, 36, 8059)
    G.addVertice(18, 16, 1)
    G.addVertice(19, 117, 5085)
    G.addVertice(20, 85, 1)
    G.addVertice(21, 54, 9043)
    G.addVertice(22, 8, 1)
    G.addVertice(23, 19, 1)
    G.addVertice(24, 35, 1)
    G.addVertice(25, 76, 1)
    G.addVertice(26, 51, 1)
    G.addVertice(27, 62, 1)
    G.addVertice(28, 2, 1)
    G.addVertice(29, 66, 2924)
    G.addVertice(30, 8, 1)
    G.addVertice(31, 83, 1)
    G.addVertice(32, 39, 1)

    # Arestas
    # I Plano Piloto
    G.addAresta(0, 3)
    G.addAresta(0, 15)
    G.addAresta(0, 4)
    G.addAresta(0, 17)
    G.addAresta(0, 15)
    G.addAresta(0, 18)
    G.addAresta(0, 9)
    G.addAresta(0, 21)
    G.addAresta(0, 10)
    G.addAresta(0, 28)
    G.addAresta(0, 24)
    G.addAresta(0, 29)
    G.addAresta(0, 2)
    # II Gama
    G.addAresta(1, 14)
    G.addAresta(1, 20)
    G.addAresta(1, 23)
    G.addAresta(1, 12)
    # III Taguatinga
    G.addAresta(2, 3)
    G.addAresta(2, 29)
    G.addAresta(2, 19)
    G.addAresta(2, 32)
    G.addAresta(2, 16)
    G.addAresta(2, 20)
    G.addAresta(2, 11)
    G.addAresta(2, 8)
    # IV Brazlândia
    G.addAresta(3, 25)
    G.addAresta(3, 8)
    # V Sobradinho
    G.addAresta(4, 30)
    G.addAresta(4, 5)
    G.addAresta(4, 27)
    G.addAresta(4, 17)
    G.addAresta(4, 25)
    # VI Planaltina
    G.addAresta(5, 30)
    G.addAresta(5, 27)
    G.addAresta(5, 6)
    # VII Paranoá
    G.addAresta(6, 27)
    G.addAresta(6, 26)
    G.addAresta(6, 13)
    G.addAresta(6, 17)
    # VIII Núcleo Bandeirante
    G.addAresta(7, 9)
    G.addAresta(7, 18)
    G.addAresta(7, 13)
    G.addAresta(7, 16)
    G.addAresta(7, 32)
    # IX Ceilândia
    G.addAresta(8, 31)
    G.addAresta(8, 11)
    # X Guará
    G.addAresta(9, 28)
    G.addAresta(9, 21)
    G.addAresta(9, 18)
    G.addAresta(9, 13)
    G.addAresta(9, 19)
    G.addAresta(9, 29)
    # XI Cruzeiro
    G.addAresta(10, 21)
    G.addAresta(10, 28)
    # XII Samambaia
    G.addAresta(11, 31)
    G.addAresta(11, 20)
    G.addAresta(11, 14)
    # XIII Santa Maria
    G.addAresta(12, 23)
    G.addAresta(12, 26)
    # XIV São Sebastião
    G.addAresta(13, 26)
    # XV Recanto das Emas
    G.addAresta(14, 20)
    # XVI Lago Sul
    G.addAresta(15, 23)
    G.addAresta(15, 16)
    # XVII Riacho Fundo
    G.addAresta(16, 23)
    G.addAresta(16, 20)
    G.addAresta(16, 32)
    # XVIII Lago Norte
    G.addAresta(17, 22)
    G.addAresta(17, 25)
    G.addAresta(17, 27)
    # XIX Candangolândia
    G.addAresta(18, 23)
    # XX Águas Claras
    G.addAresta(19, 29)
    G.addAresta(19, 32)
    G.addAresta(19, 23)
    # XXI Riacho Fundo 2
    G.addAresta(20, 23)
    # XXII Sudoeste/Octogonal
    G.addAresta(21, 28)
    # XXIII Varjão
    # XXIV Park Way
    G.addAresta(23, 26)
    # XXV Estrutural/Scia
    G.addAresta(24, 28)
    G.addAresta(24, 29)
    # XXVI Sobradinho II
    G.addAresta(25, 30)
    # XXVII Jardim Botânico
    # XXVIII Itapoã
    # XXIX SIA
    G.addAresta(28, 29)
    # XXX Vicente Pires
    # XXXI Fercal
    # XXXII Sol Nascente/Pôr do Sol
    # XXXIII Arniqueira

    total = 0
    quant_vertices_preenchidos = len(G.graph_dict.keys())
    for i in range(len(G.graph_dict.keys())):
        if G.graph_dict[i]["armazenamento"] == 1:
            quant_vertices_preenchidos = quant_vertices_preenchidos - 1
        else:
            total = total + G.graph_dict[i]["armazenamento"]
    media = int(total / quant_vertices_preenchidos)

    for i in range(len(G.graph_dict.keys())):
        if G.graph_dict[i]["armazenamento"] == 1:
            G.graph_dict[i]["armazenamento"] = media
    return G
