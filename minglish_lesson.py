def answer(words):
    # print(words)
    graph = make_graph(words)
    # print(graph)
    start = start_vertex(graph)
    # print(start)

    letters = []
    seen = []

    # DFS postorder graph traversal
    def traverse(vertex):
        if vertex not in seen:
            seen.append(vertex)
            if vertex in graph:
                for edge in graph[vertex]:
                    traverse(edge)
            letters.append(vertex)

    traverse(start)

    # topological sort - reverse DFS postorder
    ordered = letters[::-1]
    alphabet = stringify(ordered)
    return alphabet

def stringify(letters):
    alphabet = ''
    for letter in letters:
        alphabet += letter
    # print(alphabet)
    return alphabet

def make_graph(words):
    graph = {}
    for i in range(1, len(words)):
        pair = find_edge(words[i-1], words[i])
        # print(pair)
        if pair is not None:
            vertex, edge = pair
            if vertex in graph:
                # add edge to vertex
                graph[vertex].append(edge)
            else:
                # create vertex, edge pair
                graph[vertex] = [edge]
    return graph

def find_edge(a, b):
    l = min(len(a), len(b))
    for i in range(l):
        if a[i] != b[i]:
            return a[i], b[i]

def start_vertex(graph):
    edges = []
    for values in graph.values():
        for val in values:
            edges.append(val)
    for vertex in graph:
        if vertex not in edges:
            return vertex

def test():
    words = ["z", "yx", "yz"]
    assert answer(words) == "xzy"
    words = ["y", "z", "xy"]
    assert answer(words) == "yzx"
    words = ["ba", "ab", "cb"]
    assert answer(words) == "bac"
    words = ["abc", "acd", "bcc", "bcd"]
    assert answer(words) == "abcd"

test()