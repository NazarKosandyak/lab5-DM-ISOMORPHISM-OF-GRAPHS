import networkx as nx
import random

# Створюємо два графи
G1 = nx.Graph()
G1.add_nodes_from([1, 2, 3, 4])
G1.add_edges_from([(1, 3), (1, 3), (2, 3), (3, 4)])

G2 = nx.Graph()
G2.add_nodes_from([1, 2, 3, 4])
G2.add_edges_from([(2, 2), (2, 4), (3, 4), (1, 4)])

# Перевіряємо, чи є графи ізоморфними
if nx.is_isomorphic(G1, G2):
    print("Графи G1 та G2 ізоморфні")
else:
    print("Графи G1 та G2 неізоморфні")

    # Якщо графи неізоморфні, випадковим чином видаляємо зв'язок з графу G2
    edge_list = list(G2.edges)
    rand_edge = random.choice(edge_list)
    G2.remove_edge(rand_edge[0], rand_edge[1])
    print(f"Граф G2 модифіковано: видалено зв'язок {rand_edge}")

    # Перевіряємо, чи стали графи ізоморфними після модифікації
    if nx.is_isomorphic(G1, G2):
        print("Граф G2 успішно змінено: тепер він ізоморфний графу G1")
    else:
        print("Граф G2 не може бути змінений, щоб був ізоморфний графу G1")