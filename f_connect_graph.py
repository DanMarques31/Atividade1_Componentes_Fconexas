# import para construção e plot do grafo
import networkx as nx
import matplotlib.pyplot as plt

# Calcula as componentes fortemente conectadas com a func strongly_connected_components() da networkx
def calcular_cfc(grafo):
    
    cfc = list(nx.strongly_connected_components(grafo))
    return cfc

# Nome do arquivo de entrada
input_file = "graph.txt"

# Cria um grafo direcionado usando NetworkX
grafo = nx.DiGraph()

# Abre e Lê o arquivo, faz as mudanças na string para montar o grafo e monta-o
with open(input_file, 'r') as graph:
    
    linhas = graph.readlines()
    data = [linha.strip().split() for linha in linhas]
    grafo.add_edges_from(data)


# Calcule o fecho transitivo direto
fecho_transitivo = nx.transitive_closure(grafo)

# Chamada da função que retorna as componentes f-conexas
cfc_result = calcular_cfc(grafo)

# Imprime o resultado
print("componentes fortemente conectadas:")
for componente in cfc_result :
    print(componente)

# Plota o grafo
nx.draw(grafo, with_labels = True, node_size = 500, node_color = 'lightblue', font_size = 12, font_color = 'black', font_weight = 'bold', arrowsize = 20)
plt.show()