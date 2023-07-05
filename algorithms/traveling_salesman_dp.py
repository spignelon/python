# Travelling salesman problem using Dynamic Programming
from itertools import permutations
V = 4

def travel_salesman_problem(graph, s):
    # store all vertices
    vertex = []
    for i in range(V):
        if i != s:
            vertex.append(i)
            # print(vertex)
    
    min_path = []
    next_permutation = permutations(vertex)

    for i in next_permutation:
        current_pathweight = 0
        k = s
        for j in i:
            current_pathweight += graph[k][j]
            k = j
        current_pathweight += graph[k][s]
        min_path.append(current_pathweight)
        x = sorted(min_path)
    return x[0]

if __name__ == "__main__":
    # matrix representation of graph
    graph = [[0, 10, 15, 20],
             [10, 0, 35, 25],
             [15, 35, 0, 30],
             [20, 25, 30, 0]]
    s = 0
    print(travel_salesman_problem(graph, s))
