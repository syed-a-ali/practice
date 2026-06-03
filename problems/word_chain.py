from typing import List
from collections import defaultdict

def word_chain(words: List[str]) -> bool:
    """
    Given a list of words, determine whether the words can be chained to form a circle.
    A word X can be placed in front of another word Y in a circle if the last character
    of X is same as the first character of Y.

    For example, the words ['chair', 'height', 'racket', touch', 'tunic']
    can form the following circle:
    chair --> racket --> touch --> height --> tunic --> chair
    """
    if not words:
        return True

    # Model as a directed graph: each word is an edge from word[0] -> word[-1].
    # A circular chain exists iff an Eulerian circuit exists, which requires:
    #   1. in-degree == out-degree for every node
    #   2. all nodes are strongly connected
    graph = defaultdict(set)
    reverse_graph = defaultdict(set)
    in_degree = defaultdict(int)
    out_degree = defaultdict(int)
    nodes = set()

    for word in words:
        u, v = word[0], word[-1]
        graph[u].add(v)
        reverse_graph[v].add(u)
        out_degree[u] += 1
        in_degree[v] += 1
        nodes.add(u)
        nodes.add(v)

    for node in nodes:
        if in_degree[node] != out_degree[node]:
            return False

    def reachable(start, g):
        visited = {start}
        stack = [start]
        while stack:
            node = stack.pop()
            for neighbor in g[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    stack.append(neighbor)
        return visited

    start = next(iter(nodes))
    return reachable(start, graph) == nodes and reachable(start, reverse_graph) == nodes
