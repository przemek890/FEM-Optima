import numpy as np
""""""""""""""""""""""""""""""""""""""""""
points_2 = [np.sqrt(1/3),-np.sqrt(1/3)]
weights_2 = [1.0,1.0]
points_3 = [np.sqrt(3/5),0,-np.sqrt(3/5)]
weights_3 = [5/9,8/9,5/9]
points_4 = [np.sqrt(3/7 + 2/7 * np.sqrt(6/5)),np.sqrt(3/7 - 2/7 * np.sqrt(6/5)),-np.sqrt(3/7 - 2/7 * np.sqrt(6/5)),-np.sqrt(3/7 + 2/7 * np.sqrt(6/5))]
weights_4 = [(18 - np.sqrt(30))/ 36,(18 + np.sqrt(30))/ 36,(18 + np.sqrt(30))/ 36,(18 - np.sqrt(30))/ 36]
gauss = {"w2":weights_2,"p2":points_2,"w3":weights_3,"p3":points_3,"w4":weights_4,"p4":points_4}
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""" # Okreslam kolejnosc punktow calkowania
tab_p2 = [(x, y) for x in reversed(gauss["p2"]) for y in reversed(gauss["p2"])]
tab_p3 = [(x, y) for x in reversed(gauss["p3"]) for y in reversed(gauss["p3"])]
tab_p4 = [(x, y) for x in reversed(gauss["p4"]) for y in reversed(gauss["p4"])]
gauss_points = {"p2":tab_p2,"p3":tab_p3,"p4":tab_p4}
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""" # Okreslam kolejnosc wag
tab_w2 = [(w1, w2) for w1 in reversed(gauss["w2"]) for w2 in reversed(gauss["w2"])]
tab_w3 = [(w1, w2) for w1 in reversed(gauss["w3"]) for w2 in reversed(gauss["w3"])]
tab_w4 = [(w1, w2) for w1 in reversed(gauss["w4"]) for w2 in reversed(gauss["w4"])]
gauss_weights = {"w2":tab_w2,"w3":tab_w3,"w4":tab_w4}
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""" # Okreslam kolejnosc punktow calkowania na brzegach
def generate_combinations_points(points):
    com_down = []
    com_right = []
    com_top = []
    com_left = []
    for i in reversed(gauss[f"p{points}"]):   # dolny bok
        com_down.append((i,-1.))
    for i in reversed(gauss[f"p{points}"]):   # prawy bok
        com_right.append((1.,i))
    for i in gauss[f"p{points}"]:   # gorny bok
        com_top.append((i,1))
    for i in gauss[f"p{points}"]:   # lewy bok
        com_left.append((-1,i))
    return {"edge_d":com_down,"edge_r":com_right,"edge_t":com_top,"edge_l":com_left}
edges_2 = generate_combinations_points(2)  # słownik 4 krawędzi kazda krawedz po 2 punktow
edges_3 = generate_combinations_points(3)  # słownik 4 krawędzi kazda krawedz po 3 punktow
edges_4 = generate_combinations_points(4)  # słownik 4 krawędzi kazda krawedz po 4 punktow



