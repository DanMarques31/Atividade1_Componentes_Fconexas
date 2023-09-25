# Daniel Luiz Araújo Marques     Componentes f-conexas em python

# import para construção e plot do grafo
import networkx as nx
import matplotlib.pyplot as plt

def find_strongComponents(grafo):
    components = []  # Lista para armazenar as componentes fortemente conectadas
    visited = set()  # Conjunto de vértices visitados

    def deepSearch(vInicial, componente):
        componente.add(vInicial)  # Adiciona o vértice inicial à componente atual
        visited.add(vInicial)  # Marca o vértice inicial como visitado

        for vizinho in grafo.neighbors(vInicial):
            if vizinho not in visited:
                deepSearch(vizinho, componente)  # Chama a função até todos vizinhos estarem visitados

    for initNode in grafo.nodes():
        if initNode not in visited:  
            nova_componente = set()  # Cria um conjunto para armazenar a nova componente
            deepSearch(initNode, nova_componente)  # Inicia uma busca em profundidade a partir do vértice inicial
            components.append(nova_componente)  # Adiciona a nova componente à lista de componentes

    return components

# Nome do arquivo de entrada
input_file = "graph.txt"

# Cria um grafo direcionado usando NetworkX
grafo = nx.DiGraph()

# Abre e Lê o arquivo, faz as mudanças na string para montar o grafo e monta-o
with open(input_file, 'r') as graph:
    linhas = graph.readlines()
    data = [linha.strip().split() for linha in linhas]
    grafo.add_edges_from(data)

# Chamada da função que retorna as componentes f-conexas
find_strongComponents_result = find_strongComponents(grafo)

# Imprime o resultado
print("Componentes F-Conexas:")
for componente in find_strongComponents_result:
    print(list(componente))

# Plot do grafo original
plot = nx.spring_layout(grafo)
nx.draw(grafo, plot, with_labels = True, node_size = 550, node_color = 'cyan', font_size = 16, font_color = 'black', font_weight = 'bold', arrowsize = 25)
plt.show()