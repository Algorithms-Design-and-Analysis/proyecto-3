import sys
from collections import deque
from itertools import chain

def solve(graph, weights):
    # Precompute neighbors
    neighbors = [set(graph[v]) for v in range(len(graph))]

    # Sort vertices by weight
    vertices = sorted(range(len(graph)), key=lambda v: weights[v], reverse=True)

    # Start with an empty clique and a set of all vertices
    clique = []
    total = 0
    remaining = set(vertices)

    # While the set of vertices is not empty...
    for v in vertices:
        if v not in remaining:
            continue

        # Check if adding v to the clique would result in a non-clique
        if any(w not in neighbors[v] for w in clique):
            continue

        # Add v to the clique and update remaining vertices
        clique.append(v)
        total += weights[v]
        remaining.remove(v)

    return total, clique

def main():
    # python greedy.py < input.in > output.out
    cases = int(sys.stdin.readline())
    for _ in range(cases):
        weights = [int(x) for x in sys.stdin.readline().split()]
        n = len(weights)
        graph = [[] for _ in range(n)]
        for i in range(n):
            edges = [int(x) for x in sys.stdin.readline().split()]
            for j in edges:
                graph[i].append(j-1)
                graph[j-1].append(i)

        ans = solve(graph, weights)
        print(f"{ans[0]} {' '.join([str(x+1) for x in ans[1]])}")

if __name__ == "__main__":
    main()